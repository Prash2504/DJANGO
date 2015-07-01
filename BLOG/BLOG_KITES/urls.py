from django.conf.urls import url,patterns
from BLOG_KITES import views


urlpatterns = patterns( '',
		          url(r'^$',views.home,name ='home'), 
		          url(r'home$',views.home,name ='home'), 
		          url(r'Services$',views.services,name ='services'),
                  url(r'News & Publications$',views.services,name ='news_publications'),                     
                      )

 



