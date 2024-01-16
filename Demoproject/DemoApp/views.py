from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Team,Destination

# Create your views here.
def home(req):
    data=Place.objects.all()
    name=Team.objects.all()
    return render(req,'index.html',{'data':data,'name':name})

def contact(req):
    return render(req,'contact.html')
def news(req):
    return render(req,'news.html')

def destinations(req):
    data=Destination.objects.all()
    return render(req,'destinations.html',{'data':data})

def elements(req):
    return render(req,'elements.html')

