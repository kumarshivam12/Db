from django.db import models
import datetime
import random

# Create your models here.

class role_per(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    role=models.CharField(max_length=250)
    perr=models.TextField()



class consumer_Db(models.Model):
    User_type=models.CharField(max_length=250)
    Empid = models.ForeignKey('role_per',on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    Fname = models.CharField(max_length=250)
    Mname = models.CharField(max_length=250)
    Lname = models.CharField(max_length=250)
    Email=models.EmailField(max_length=250)
    Phone=models.PositiveIntegerField(max_length=10)
    Address=models.TextField()
    Mgname=models.CharField(max_length=250)
    Mg_email=models.CharField(max_length=250)
    Location=models.TextField()




