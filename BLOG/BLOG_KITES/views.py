from django.shortcuts import render_to_response
from BLOG_KITES.models import Menu,Services,News_Publications
from django.http import HttpResponse
import time
  
# Create your views here.

def MENU():
    MENU_LISTS = []
    
    for menu in Menu.objects.all():
        MENU_LISTS.append(menu) 
   
    return MENU_LISTS 

def NEWS():
    News_Pub = [] 
    for news in News_Publications.objects.filter(Date__year="%s"%time.strftime("%Y"),Date__month="%s"%time.strftime("%m")).order_by(-Date):
         News_Pub.append(
                  {  'Month':news.Month,
                     'Year' :news.Year,
                     'Data' :news.Data
                  }
             )
    return News_Pub

def home(request):
   
    MENU_LIST =  MENU()
    
    return render_to_response('home.html',locals())   
    
def services(request):
    MENU_LIST =  MENU()
    services = "YET TO ADD THE SERVICES"
    return render_to_response('Services.html',locals())


def news_publications(request):
        


