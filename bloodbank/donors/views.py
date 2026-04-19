
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render,redirect
from.models import donor
from .forms import Donorform , Searchform
from django.contrib import messages
from django.contrib.auth import login
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
            p_name=request.POST.get('name')
            sbldgrp = request.POST.get('bldgrp')
            stime = request.POST.get('urgency')
            division = request.POST.get('division')
            district = request.POST.get('district')
            
            
            edonor=donor.objects.filter(bldgrp=sbldgrp)
                
            if edonor.exists():
                if division:
                    edonor = edonor.filter(division=division)
                if district:
                    edonor = edonor.filter(district=district)
                

                if stime:
                    today = timezone.now().date()
                    if stime == "asap":
                        mindate = today - timedelta(days=90)
                        edonor = edonor.filter(Q(donation_date__lte=mindate) | Q(donation_date__isnull=True))
                    elif stime == "custom":
                        from_time = request.POST.get('fromtime', '')
                        to_time = request.POST.get('totime', '')
                edonor=edonor.distinct()
                       
            else:
                messages.error(request, 'There is No eligible Donor !')
            s_key=f"{sbldgrp}_{division}_{district}_{p_name}"
            if s_key not in request.session:

             sform.save()
             request.session[s_key] =True
            else:
                messages.warning(request, 'You have already saved this blood group request in this session!') 
            edonor=edonor.distinct()
            return render(request, 'searchdonor.html', {'edonor': edonor})
        else:
            messages.error(request, 'There is an error in the Search form!')
            return redirect('Homepage')
        