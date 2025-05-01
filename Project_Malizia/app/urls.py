# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('why-choose-us/', views.why_choose_us, name='why_choose_us'),
]
