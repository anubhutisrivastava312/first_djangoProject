from django.db import models
from django.utils import timezone

# Create your models here.
class Tournament(models.Model):
    t_name= models.CharField(max_length=50,null=False)
    t_description=models.TextField()
    t_venue=models.CharField(max_length=100)
    t_start_date=models.DateField(default=timezone.now)
    t_end_date=models.DateField(default=timezone.now)
    t_age_group=models.CharField(max_length=20)

Gender=[

    ("M","Male"),
    ("F","Female"),
]    



class Enrollment(models.Model):
    name=models.CharField(max_length=60,null=False) 
    age=models.IntegerField()
    email=models.EmailField(max_length=50,null=False)  
    phone=models.CharField(max_length=50,null=False)
    city=models.CharField(max_length=50,null=False)
    address=models.TextField()
    tournament_name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=6,choices=Gender,null=False)
    date=models.DateField(default=timezone.now)