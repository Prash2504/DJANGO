from django.db import models



Months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# Create your models here.

class Menu(models.Model):
    Name = models.CharField(max_length = 20)
    pub_date = models.DateTimeField('pub_date' )

    def __str__(self):
         return self.Name 


class Services(models.Model):
    service_name = models.CharField(max_length = 300)


class News_Publications(models.Model):
    Month  = models.CharField(max_length = 20,choices = Months) 
    Year   = models.CharField(max_length = 6) 
    Data   = models.CharField(max_length = 200) 
   
    def __str__(self):
        return Month_Year,Data   
