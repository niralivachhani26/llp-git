from django.shortcuts import render,get_object_or_404
from .models import Service

def home(request):
    services = Service.objects.all()[:3]
    return render(request, 'services/home.html', {'services': services})

def service_detail(request, id):
    service = get_object_or_404(Service, id=id)  # Get the specific service by its ID
    return render(request, 'services/service_detail.html', {'service': service})

def all_services(request):
    services = Service.objects.all()
    return render(request, 'services/all_services.html', {'services': services})
