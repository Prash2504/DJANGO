from django.db import models



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


class News_Publications(models.Model):
    Current_Month  = models.CharField("Month",max_length = 20,choices = Months) # 
    Year   = models.CharField(max_length = 6) 
    Data   = models.CharField(max_length = 200) 
    
    def __str__(self):
        return "%s %s"%(self.Current_Month,self.Year)   
