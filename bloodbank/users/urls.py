
from django.urls import path
from . import views

urlpatterns = [
    path('userlogin', views.userlogin, name='UserLogin'),
    path('userlogout', views.userlogout, name='UserLogout'),
    path('admin-dashboard/', views.admindash, name='AdminDashboard'),
    path('donor-dashboard/', views.donordash, name='DonorDashboard'),
    
    path('delete-donor/<int:donor_id>', views.delete_donor , name='DeleteDonor'),
    path('search-request', views.searchreq, name='SearchRequest'),
    path('delete-request/<int:search_id>', views.delrequest, name='DeleteRequest'),
    path('pending-request/<int:donor_id>', views.p_request, name='PendingRequests'),
    path('responding/<int:request_id>', views.respond, name='Respond'),
    

]