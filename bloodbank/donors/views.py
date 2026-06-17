
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render,redirect
from.models import donor
from .forms import Donorform , Searchform , Searchform_L,EditDonorForm
from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.db.models import Q



def homepage(request):
    return render(request , 'page1.html',{})
def reg(request):
    return render (request, 'page2.html',{})
def req(request):
     return render (request, 'page3.html',{})

def why(request):
    return render (request ,'why.html',{} )
def regdonor(request):
   
    if request.method == "POST":
        form = Donorform(request.POST)
        if form.is_valid():
            user = form.save(commit=True) 
            
            donor_bio = donor.objects.get(user=user)
            donor_bio.hiv = bool(request.POST.get('hiv')) 
            donor_bio.hep= bool(request.POST.get('hep') )
            donor_bio.hypertension = bool(request.POST.get('hypertension')) 
           
            donor_bio.no_disease = bool(request.POST.get('no_disease')) 
            donor_bio.save()  

            if donor_bio.hiv or donor_bio.hep:
                messages.error(request, 'Sorry! Your request has been denied due to health condition')
                user.delete()
                return redirect('Homepage')

            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('DonorDashboard')
        else:
            return render(request, 'page2.html', {'form': form})
    else:
        form = Donorform()
        return render(request, 'page2.html', {'form': form})
   
def donorlist(request):
    if request.method == "POST":
        sform=Searchform(request.POST)
        if sform.is_valid():
           
            sbldgrp = request.POST.get('bldgrp')
            snum=request.POST.get('num')
           
            
            
            edonor=donor.objects.filter(bldgrp=sbldgrp)
                
            if edonor.exists():
                
                edonor=edonor.distinct()
                       
            else:
                messages.error(request, 'There is No eligible Donor !')
           
            edonor=edonor.distinct()
            return render(request, 'searchdonor.html', {'edonor': edonor ,'sbldgrp': sbldgrp,'snum':snum})
        else:
            messages.error(request, 'There is an error in the Search form!')
            return redirect('Homepage')
def location_search(request):
  sbldgrp=request.GET.get('bldgrp','').replace(' ','+')
  snum=request.GET.get('num','') 
  if not sbldgrp and not snum:
      messages.error(request,'No blood group Specified') 
      return redirect('Homepage') 
  return render(request,'page3.2.html',{'sbldgrp':sbldgrp , 'snum':snum})  
  
  
   
def d_list_location(request):
    if request.method == "POST":
        sform=Searchform_L(request.POST)
        if sform.is_valid():
           
            sbldgrp = request.POST.get('bldgrp')
            snum=request.POST.get('num')
           
            division = request.POST.get('division')
            district = request.POST.get('district')
            
            
            edonor=donor.objects.filter( division=division , district=district)
                
           
            s_key=f"{sbldgrp}_{division}_{district}_{snum}"
            if s_key not in request.session:
             instance = sform.save(commit=False)
             instance.bldgrp = sbldgrp        
             instance.num = snum              
             instance.save()
             request.session[s_key] = True
             
            else:
                messages.warning(request, 'You have already saved this blood group request in this session!') 
            if not edonor.exists():
                messages.error(request,'There is no eligible donor!')
            return render(request, 'locationsearch.html', {'edonor': edonor,'sbldgrp':sbldgrp,'snum':snum})
        else:
            messages.error(request, 'There is an error in the Search form!')
            return redirect('Homepage')
def editprofile(request):
    donor_bio = request.user.donor_bio

    if request.method == "POST":
        form = EditDonorForm(request.POST)

        if form.is_valid():
           
            user = request.user
            user.username = form.cleaned_data['username']

            new_password = form.cleaned_data.get('new_password1')
            if new_password:
                user.set_password(new_password)
                update_session_auth_hash(request, user)

            user.save()

           
            donor_bio.email        = form.cleaned_data['email']
            donor_bio.phone        = form.cleaned_data['phone']
            donor_bio.division     = form.cleaned_data['division']
            donor_bio.district     = form.cleaned_data['district']
            donor_bio.upazila      = form.cleaned_data['upazila']
            donor_bio.area         = form.cleaned_data['area']
            donor_bio.postcode     = form.cleaned_data['postcode']
            donor_bio.donation_date = form.cleaned_data['donation_date'] or None

            
            donor_bio.hiv          = bool(request.POST.get('hiv'))
            donor_bio.hep          = bool(request.POST.get('hep'))
            donor_bio.hypertension = bool(request.POST.get('hypertension'))
            donor_bio.no_disease   = bool(request.POST.get('no_disease'))

            donor_bio.save()

            messages.success(request, 'Profile updated successfully!')
            return redirect('DonorDashboard')

        else:
            return render(request, 'profile.html', {'form': form, 'donor_bio': donor_bio})

    else:
        form = EditDonorForm(initial={
            'username'      : request.user.username,
            'email'         : donor_bio.email,
            'phone'         : donor_bio.phone,
            'division'      : donor_bio.division,
            'district'      : donor_bio.district,
            'upazila'       : donor_bio.upazila,
            'area'          : donor_bio.area,
            'postcode'      : donor_bio.postcode,
            'donation_date' : donor_bio.donation_date,
        })

    return render(request, 'profile.html', {'form': form, 'donor_bio': donor_bio})