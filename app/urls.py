# app/urls.py
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('clients/', views.clients, name='clients'),
    path('api/chatbot/', views.chatbot_endpoint, name='chatbot_endpoint'),  # Add this new line
]
