from dotenv import load_dotenv
import os
import base64
import requests
import json


#load environment variables from .env
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#get token from spotify api
def get_token():
    auth_string = client_id+":"+client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes),'utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization":"Basic "+auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type":"client_credentials"}

    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization":"Bearer "+token}

def get_track_details(track_id, token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)

    
    data = response.json()
    return data

#test run
track_id = "14gmLQPNYokqB8OKxAp69f"
token = get_token()

track_data = get_track_details(track_id, token)
print(track_data)

