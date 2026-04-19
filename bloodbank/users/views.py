from datetime import timedelta

from django.utils import  timezone

from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from donors.models import donor,searchdonor
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect

def userlogin(request):
     if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user_type=='admin':
                if user.is_staff or user.is_superuser:
                 login(request, user)
                 messages.success(request,"Admin logged in successfully !")
                 return redirect('AdminDashboard')
                else:
                  messages.error(request, 'Access denied. This is not an admin account.')
            elif user_type=='donor':
                if hasattr(user, 'donor_bio'):
                 login(request, user)
                 messages.success(request, 'Donor login successful!')
                 return redirect('DonorDashboard')
                else:
                   
                    messages.error(request, 'No donor profile  found. Please register as a donor first.')
                    return render(request, 'login.html', {})
     
        else:
           messages.error(request, 'Invalid username or password!')
     else:
        return render(request, 'login.html', {})
     return render(request, 'login.html', {})
         
 
def userlogout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('Homepage')

@login_required

def admindash(request) :
     
    tdonors = donor.objects.count()
    trequests=searchdonor.objects.count()
    bld_grps_cnt = donor.objects.values('bldgrp').distinct().count()
    
    alldonors = donor.objects.all().order_by('-id')[:50]
    
    return render(request, 'admindash.html', {
        'totalrequest': trequests,
        'totaldonors': tdonors,
        'totalbldgrp': bld_grps_cnt,
        'all_donors': alldonors
    })
@login_required
def donordash(request) :
    
    try:
        donor_info = donor.objects.filter(user=request.user).first()
    except:
        donor_info = None
    
    return render(request, 'donordash.html', {
        'donor_info': donor_info
    })


def delete_donor(request, donor_id):
    if donor.objects.filter(id=donor_id).exists():
        donor_bio= donor.objects.get(id=donor_id)
        user=donor_bio.user

        user.delete()
        messages.success(request, 'Donor Deleted Successfully!')
        return redirect('AdminDashboard')
    else:
        messages.error(request, 'Donor not Found!')

    return redirect('Admin Dashboard')
def searchreq(request):
    searchr=searchdonor.objects.all()
    return render(request,'request.html',{'searchrequest': searchr})
def delrequest(request , search_id):
     if searchdonor.objects.filter(id=search_id).exists():
        search= searchdonor.objects.get(id=search_id)
        search.delete()
        messages.success(request, 'Request Deleted Successfully!')
        return redirect('SearchRequest')
     else:
        messages.error(request, 'Request not Found!')

     return redirect('Admin Dashboard')
def p_request(request , donor_id):
    if donor.objects.filter(id=donor_id).exists():              
        d_profile=donor.objects.get(id=donor_id)
        requests=searchdonor.objects.filter(bldgrp=d_profile.bldgrp , accepted=False)
        return render(request , 'pending.html', {'requests': requests})
    else:
        messages.error(request, 'Donor not found!')
        return redirect('UserLogin') 
def  respond(request, request_id) :
    blood_request = get_object_or_404(searchdonor, id=request_id)
    donor_bio = request.user.donor_bio  # the logged in donor


    send_mail(
        subject='A donor is on the way!',
        message=f'Hello, donor {donor_bio.fullname} with blood group {donor_bio.bldgrp} has responded to your request. Contact: {donor_bio.phone}',
        from_email='sarasubah14@gmail.com',
        recipient_list=[blood_request.email],  # requester's email
    )


    blood_request.accepted = True
    blood_request.save()
    messages.success(request, 'Successfully responded!')
    return redirect('DonorDashboard')


    

    

