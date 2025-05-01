from django.shortcuts import render

from app.models import Features


# Create your views here.
def why_choose_us(request):
    feature=Features.objects.all()
    return render(request,'why_choose_us.html',{'features':feature})