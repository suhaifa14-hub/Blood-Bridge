from django.db import models
from django.contrib.auth.models import User


class donor(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE , null=True , blank=True , related_name= 'donor_bio')
    
    
    fullname = models.CharField(max_length=100)
    age=models.DateField(null=True, blank=True)
    
    email = models.EmailField(null=True , unique=True , default='')
    phone = models.CharField(max_length=15,unique=True)
    bldgrp = models.CharField(max_length=3, choices=[
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ])
    division = models.CharField(max_length=20, choices=[
        ( 'dhaka','Dhaka'),
        ( 'chattogram','Chattogram'),
        ( 'rajshahi','Rajshahi'),
        ( 'khulna','Khulna'),
        ( 'barishal','Barishal'),
        ( 'sylhet','Sylhet'),
        ( 'rangpur','Rangpur'),
        ( 'mymensingh','Mymensingh'),
    ])
    district = models.CharField(max_length=50)
    upazila=models.CharField(max_length=50,null=True)
    area=models.CharField(max_length=50,null=True)
    postcode=models.CharField(max_length=50,null=True)
    
    h_address=models.CharField(max_length=200, default='')
    donation_date = models.DateField(null=True, blank=True)
    
  
    
    hypertension = models.BooleanField(default=False)
    
    
    hiv=models.BooleanField(default=False)
    hep=models.BooleanField(default=False)

    no_disease=models.BooleanField(default=False)
    
    
    
    
    def __str__(self):
        return f"{self.fullname} - {self.bldgrp}"
    
class searchdonor(models.Model):
     
     
     
     num=models.CharField(max_length=11, unique=True , null=True , blank=True)
     bldgrp = models.CharField(max_length=3, choices=[
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ])
     
     email = models.EmailField(unique=True, null=True, blank=True)
     division = models.CharField(max_length=20, choices=[
        ( 'dhaka','Dhaka'),
        ( 'chattogram','Chattogram'),
        ( 'rajshahi','Rajshahi'),
        ( 'khulna','Khulna'),
        ( 'barishal','Barishal'),
        ( 'sylhet','Sylhet'),
        ( 'rangpur','Rangpur'),
        ( 'mymensingh','Mymensingh'),
    ])
     district = models.CharField(max_length=50)
     accepted=models.BooleanField(default=False)
    
    
       
    
     
     def __str__(self):
        return f"{self.bldgrp} | {self.division} | {self.num}"





