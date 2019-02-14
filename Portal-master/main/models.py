from django.db import models
import datetime
import random

# Create your models here.
class consumer(models.Model):
    User_type=models.CharField(max_length=250)
    Empid = models.PositiveIntegerField(max_length=250)
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



class cabprosessing(models.Model):
    requestid=models.PositiveIntegerField()
    servicetype=models.CharField(max_length=250)
    source=models.CharField(max_length=250)
    destnation=models.CharField(max_length=250)
    Date=models.DateField()
    Pickuptime=models.TimeField()
    issuedto=models.CharField(max_length=250)
    Empid=models.PositiveIntegerField()
    Drivername=models.CharField(max_length=250)
    status=models.CharField(max_length=250)
    fare=models.PositiveIntegerField()
    location=models.CharField(max_length=250)

class History(models.Model):
    requestid=models.PositiveIntegerField()
    Date=models.DateField()
    Time=models.TimeField()
    Servicetype=models.CharField(max_length=250)
    Source=models.CharField(max_length=250)
    Destination=models.CharField(max_length=250)
    Driversname=models.CharField(max_length=250)
    fare=models.PositiveIntegerField()
    ratings=models.PositiveIntegerField()