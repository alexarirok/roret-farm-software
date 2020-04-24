from django.urls import path  
from profiles import views 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact/', views.contact, name = 'contact'),
    path('base/', views.base, name = 'base'),
    path('profile/', views.profile, name = 'profile')

]