from django import forms
from.models import donor, searchdonor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Donorform(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    fullname = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(min_value=18, max_value=65, required=True)
    email = forms.EmailField(required=True)
    weight = forms.IntegerField(min_value=40, required=True)
   
    phone = forms.CharField(max_length=15, required=True)
    bldgrp = forms.ChoiceField(choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
    ], required=True)
    division = forms.ChoiceField(choices=[
        ('dhaka', 'Dhaka'), ('chattogram', 'Chattogram'), ('rajshahi', 'Rajshahi'),
        ('khulna', 'Khulna'), ('barishal', 'Barishal'), ('sylhet', 'Sylhet'),
        ('rangpur', 'Rangpur'), ('mymensingh', 'Mymensingh'),
    ], required=True)
    district = forms.CharField(max_length=50, required=True)
    address=forms.CharField(max_length=300, required=True)
    h_address=forms.CharField(max_length=200, required=True)
    donation_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        
        user = super().save(commit=True) 
        #user.email = self.cleaned_data['email']
        
        
            
           
        donor_bio = donor.objects.create(
                user=user,  # This links to the User model
                fullname=self.cleaned_data['fullname'],
                age=self.cleaned_data['age'],
                weight=self.cleaned_data['weight'],
                
                email=self.cleaned_data['email'],
                phone=self.cleaned_data['phone'],
                bldgrp=self.cleaned_data['bldgrp'],
                division=self.cleaned_data['division'],
                district=self.cleaned_data['district'],
                address=self.cleaned_data['address'],
                h_address =self.cleaned_data['h_address'],
                donation_date=self.cleaned_data['donation_date'] or None ,
               
            )
       
        
        return user
   
class Searchform(forms.ModelForm):
    class Meta:
        model=searchdonor
        fields= ['name','bloodbag','num','bldgrp','email','division','district','urgency','request_at','hlocation']
