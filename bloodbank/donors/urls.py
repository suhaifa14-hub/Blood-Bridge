from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('register', views.reg, name="RegisterForm"),
    path('request', views.req, name='Requestpage'),
    path('regdonor', views.regdonor, name='Registrationform'),
    path('donorlist', views.donorlist, name='DonorList'),
    path('awareness', views.why, name='Awareness')
]