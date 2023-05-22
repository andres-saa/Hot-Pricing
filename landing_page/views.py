from django.shortcuts import render
from landing_page.models import New

# Create your views here.

def landingMain(request):
    news = New.objects.all()
    return render(request, 'index.html',{'news':news})

def Login(request):
    return render(request, 'login.html')