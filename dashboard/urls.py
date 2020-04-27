from django.urls import path  
from dashboard import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url 

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),
]