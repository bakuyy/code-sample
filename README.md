# Chime Backend API 

This repository is part of the Chime project, a music discovery app with a Tinder-like twist, enabling users to swipe right or left on songs, create playlists, and receive tailored music recommendations. This specific code sample showcases the backend API implemented using Django, focusing on user registration, authentication, and user preference management.

## Features

- User Registration and Authentication
- User Registration: Handled through the CreateUserView endpoint, allowing users to create accounts with credentials.
- JWT Authentication: Implements token-based authentication using JSON Web Tokens (JWT), providing endpoints for:
- Token creation
 -Token refresh
 -Token validation

## User Preference Management

- Users fill out a preference form at the start of their session.
- Preferences are stored in the UserPreferences model, capturing metrics like mood and favorite genres.
- These preferences enable personalized music recommendations powered by collaborative and content-based filtering.

## Administrative Tools

- Utilizes Django’s built-in admin panel for managing user data and preferences, simplifying testing and administration.
- Spotify API Integration
- Though not fully included in this sample, the larger project integrates with the Spotify API to:
- Retrieve and queue songs.
- Access song metrics such as beats per minute, artist, length, and danceability, used for recommendations.

### Installation and Setup

### Clone the Repository:

```
git clone https://github.com/bakuyy/code-sample.git
cd code-sample/backend
```
### Create a Virtual Environment:
```
python3 -m venv venv
source venv/bin/activate
```
Install Dependencies:
```
pip install -r requirements.txt
```
### Apply Migrations:
```
python manage.py migrate
```
### Run the Development Server:
```
python manage.py runserver
```
### Access the API:
```
Visit http://127.0.0.1:8000 to interact with the API endpoints.
```
## Key Learnings

- Technical Skills
- JWT Authentication: Gained hands-on experience implementing JWT-based authentication without relying on external services.
- Django Database Integration: Leveraged Django’s built-in database for efficient user and preference management.
- Spotify API Integration: Retrieved and analyzed song data, including metrics like danceability and tempo, as part of a recommendation algorithm.

## Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.


License
This project is licensed under the MIT License. See the LICENSE file for details.
Feel free to explore the code and reach out if you have questions or suggestions!

