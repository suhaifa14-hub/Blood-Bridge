from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('register', views.reg, name="RegisterForm"),
    path('request', views.req, name='Requestpage'),
    path('regdonor', views.regdonor, name='Registrationform'),
    path('location', views.location_search, name='LocationForm'),
    path('donorlist', views.donorlist, name='DonorList'),
    path('d_list_l', views.d_list_location, name='D_List_location'),
    path('awareness', views.why, name='Awareness'),
    path('editprofile', views.editprofile, name='EditProfile'),

]