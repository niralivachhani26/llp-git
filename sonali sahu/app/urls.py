from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/<int:id>/', views.service_detail, name='service_detail'), 
    path('all-services/', views.all_services, name='all_services'),
]
