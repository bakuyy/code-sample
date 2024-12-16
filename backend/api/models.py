from django.db import models
from django.contrib.auth.models import User

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    moods = models.JSONField(default=list)  
    genres = models.JSONField(default=list)  

    def __str__(self):
        return f"{self.user.username}'s Preferences"
