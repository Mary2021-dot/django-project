# urls.py

from django.urls import path
from . import views
from .views import DeleteChildView
from .views import donate_view
from .views import donation_form, donation_success


urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('navbar/', views.navbar, name='navbar'),
    path('footer/', views.footer, name='footer'),
    path('children/', views.children_list, name='children_list'),
    path('children/<int:id>/edit/', views.edit_child, name='edit_child'),
    path('child/delete/<int:id>/', DeleteChildView.as_view(), name='delete_child'),
    
     path('contact_us/', views.contact_us, name='contact_us'),
     path('events/', views.event_list, name='event_list'),
     path('donate/', views.donate_view, name='donate_view'),

   path('login/', views.login, name='login'),
   path('signup/', views.signup, name='signup'),

   
   
 path('donate/', donation_form, name='donation_form'),
path('donate/success/', donation_success, name='donation_success'),
    

]
