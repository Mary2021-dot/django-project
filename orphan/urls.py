# urls.py

from django.urls import path
from . import views

from .views import donate_view
from .views import donation_form


urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('navbar/', views.navbar, name='navbar'),
    path('footer/', views.footer, name='footer'),
   path('about/',views.about,name='about'),
    
     path('contact_us/', views.contact_us, name='contact_us'),
     path('events/', views.event_list, name='event_list'),
     path('donate_view/', views.donate_view, name='donate_view'),

   path('login/', views.login, name='login'),
   path('signup/', views.signup, name='signup'),

   
   
 path('donation_form/', donation_form, name='donation_form'),

    

]
