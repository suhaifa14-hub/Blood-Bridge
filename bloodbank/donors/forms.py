from django import forms
from.models import donor, searchdonor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Donorform(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    fullname = forms.CharField(max_length=100, required=True)
    age = forms.DateField( required=True)
    email = forms.EmailField(required=True)
   
   
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
    upazila=forms.CharField(max_length=300, required=True)
    area=forms.CharField(max_length=300, required=True)
    postcode=forms.CharField(max_length=300, required=True)
    h_address=forms.CharField(max_length=200, required=True)
    donation_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        
        user = super().save(commit=True) 
        
        
        
            
           
        donor_bio = donor.objects.create(
                user=user,  
                fullname=self.cleaned_data['fullname'],
                age=self.cleaned_data['age'],
                
                email=self.cleaned_data['email'],
                phone=self.cleaned_data['phone'],
                bldgrp=self.cleaned_data['bldgrp'],
                division=self.cleaned_data['division'],
                district=self.cleaned_data['district'],
                upazila=self.cleaned_data['upazila'],
                 area=self.cleaned_data['area'],
                postcode=self.cleaned_data['postcode'],
                h_address =self.cleaned_data['h_address'],
                donation_date=self.cleaned_data['donation_date'] or None ,
               
            )
       
        
        return user


class EditDonorForm(forms.Form):
    username      = forms.CharField(max_length=150, required=True)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=False)
    email         = forms.EmailField(required=False)
    phone         = forms.CharField(max_length=15, required=True)
    division      = forms.ChoiceField(choices=[
        ('dhaka', 'Dhaka'), ('chattogram', 'Chattogram'), ('rajshahi', 'Rajshahi'),
        ('khulna', 'Khulna'), ('barishal', 'Barishal'), ('sylhet', 'Sylhet'),
        ('rangpur', 'Rangpur'), ('mymensingh', 'Mymensingh'),
    ], required=True)
    district      = forms.CharField(max_length=50, required=True)
    upazila       = forms.CharField(max_length=300, required=True)
    area          = forms.CharField(max_length=300, required=True)
    postcode      = forms.CharField(max_length=300, required=True)
    donation_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('new_password1')
        p2 = cleaned_data.get('new_password2')
        if p1 and p1 != p2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class Searchform(forms.ModelForm):
    class Meta:
        model=searchdonor
        fields= ['bldgrp','num']
class Searchform_L(forms.ModelForm):
    class Meta:
        model=searchdonor
        fields= ['division','district']