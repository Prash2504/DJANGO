from django.db import models
import datetime


Months = ( 
            ("Jan","Jan"),
            ("Feb","Feb"),
            ("Mar","Mar"),
            ("Apr","Apr"),
            ("May","May"),
            ("Jun","Jun"),
            ("Jul","Jul"),
            ("Aug","Aug"),
            ("Sep","Sep"),
            ("Oct","Oct"),
            ("Nov","Nov"),
            ("Dec","Dec"),
        )

# Create your models here.

class Menu(models.Model):
    Name = models.CharField(max_length = 20)
    pub_date = models.DateTimeField("pub_date" )

    def __str__(self):
         return self.Name 


class Services(models.Model):
    service_name = models.CharField(max_length = 300)


class Events(models.Model):
    Date = models.DateTimeField("Date",default=datetime.datetime.now()) 
    Data   = models.CharField(max_length = 200)         
    def __str__(self):
        return self.Data
    
class News_Present(models.Model):
    Date = models.DateTimeField("Date",default=datetime.datetime.now())  
    Data   = models.CharField(max_length = 300)  
    def __str__(self):
        return self.Data    
     
class Notice(models.Model):
    Date = models.DateTimeField("Date",default=datetime.datetime.now())  
    Data   = models.CharField(max_length = 300)           
    def __str__(self):
        return self.Data  
        
        
