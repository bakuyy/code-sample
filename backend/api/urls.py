from django.urls import path, include
from django.contrib import admin
from .views import CreateUserView,UserPreferenceView

urlpatterns = [
    path('preferences/', UserPreferenceView.as_view(), name='user_preferences')  

]