from django.conf.urls import url,patterns
from SAMAPP import views


urlpatterns = patterns( '',
		          url(r'^$',views.home,name ='index'), 
		          url(r'index$',views.home,name ='index'), 
		          url(r'Services$',views.services,name ='services'),
                  url(r'Events$',views.Events_all,name ='news'),
                  url(r'Contact Us$',views.contact,name ='contact'),                  
                      )

