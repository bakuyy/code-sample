from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserPreference

# serializer for user preferences
class UserPrefSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = ["moods", "genres"]  # moods and genres are the fields we care about

# serializer for the user model
class UserSerializer(serializers.ModelSerializer):
    # include preferences here, but it's optional
    preferences = UserPrefSerializer(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "preferences"]  # include id, username, password, and preferences
        extra_kwargs = {"password": {"write_only": True}}  # don't show the password in responses

    def create(self, validated_data):
        # get preferences data and remove it so we can handle it separately
        preferences_data = validated_data.pop('preferences', None)
        
        # create the user and hash the password automatically
        user = User.objects.create_user(**validated_data)
        
        # if there are preferences, create them for the user
        if preferences_data:
            UserPreference.objects.create(user=user, **preferences_data)
        
        return user  # return the new user

    def update(self, instance, validated_data):
        # get preferences data if it's there
        preferences_data = validated_data.pop('preferences', None)
        
        # update the user object (username, password, etc.)
        instance = super().update(instance, validated_data)
        
        # handle preferences if they were provided
        if preferences_data:
            # get existing preferences or create them if they don't exist
            user_preferences, created = UserPreference.objects.get_or_create(user=instance)
            
            # update each field in preferences
            for attr, value in preferences_data.items():
                setattr(user_preferences, attr, value)
            
            # save the updated preferences
            user_preferences.save()
        
        return instance  # return the updated user
