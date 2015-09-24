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
    Updated = models.CharField(max_length = 20,default = 'Updated On:')  
    Date = models.DateTimeField("Date",default=datetime.datetime.now()) 
    Data   = models.CharField(max_length = 200)         
    def __str__(self):
        return self.Data
    
class News_Present(models.Model):
    Updated = models.CharField(max_length = 20,default = 'Updated On:')  
    Date = models.DateTimeField("Date",default=datetime.datetime.now())  
    Data   = models.CharField(max_length = 300)  
    def __str__(self):
        return self.Data    
     
class Notice(models.Model):
    Updated = models.CharField(max_length = 20,default = 'Updated On:')  
    Date = models.DateTimeField("Date",default=datetime.datetime.now())  
    Data   = models.CharField(max_length = 300)           
    def __str__(self):
        return self.Data  
 
class Per_Value_for_Home(models.Model): 
    Corperate = models.CharField(max_length = 10,default = '40%')
    Success_Rate = models.CharField(max_length = 10,default = '60%')
    Student = models.CharField(max_length = 10,default = '100%')
    Trainings = models.CharField(max_length = 10,default = '30%') 
    def __str__(self): 
        return "Corporate = %s,Success_Rate = %s,Student = %s,Trainings = %s "%(self.Corperate,self.Success_Rate,self.Student,self.Trainings)    


    
    
        
