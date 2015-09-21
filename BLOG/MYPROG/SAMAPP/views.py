from django.shortcuts import render_to_response
from SAMAPP.models import Menu,Services,Events,Notice,News_Present 
from django.http import HttpResponse
import time
  
# Create your views here.

def MENU():
    MENU_LISTS = []
    for menu in Menu.objects.all():
        MENU_LISTS.append(menu) 
  
    return MENU_LISTS 


def home(request):   
    MENU_LIST =  MENU()
    Events_Home = [] 
    for events in Events.objects.all().order_by('-Date'):
        Events_Home.append(
                 {  
                    'Date' :events.Date,
                    'Data' :events.Data
                 }
            ) 
    return render_to_response('index.html',locals())    
    
def services(request):
    services = "YET TO ADD THE SERVICES"
    return render_to_response('service-archive.html',locals()) 
    
def Events_all(request):
    return render_to_response('events-archive.html',locals()) 
    
def contact(request):
    MENU_LIST =  MENU()      
    return render_to_response('contact.html',locals())     
    