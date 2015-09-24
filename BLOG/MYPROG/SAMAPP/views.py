from django.shortcuts import render_to_response
from SAMAPP.models import Menu,Services,Events,Notice,News_Present,Per_Value_for_Home 
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
    notice_home = []
    news_home = [] 
    for events in Events.objects.all().order_by('-Date'):
        Events_Home.append(
                 {  
                    'Updated':events.Updated,
                    'Date' :events.Date,
                    'Data' :events.Data
                 }
            ) 
            
    for notice in Notice.objects.all().order_by('-Date'):        
        notice_home.append(
                 {  
                    'Updated':notice.Updated,
                    'Date' :notice.Date,
                    'Data' :notice.Data
                 }
            ) 

    for news in News_Present.objects.all().order_by('-Date'):        
        news_home.append(
                 {  
                    'Updated':notice.Updated,
                    'Date' :news.Date,
                    'Data' :news.Data
                 }
            ) 
            
    for Value in Per_Value_for_Home.objects.all():  
        values_home = [] 
        values_home.append( 
                 {  
                    'Corparate':Value.Corperate,
                    'Success' :Value.Success_Rate,
                    'Student' :Value.Student,
                    'Training' :Value.Trainings,
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
    