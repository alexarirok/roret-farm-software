from django.urls import path  
from dashboard import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url 

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),
    url(r'^dashboard/livestock_create/$', views.livestock_create, name = 'livestock_create'),
    url(r'^dashboard/livestock_list/$', views.livestock_list, name = 'livestock_list'),
    url(r'^dashboard/save_livestock_form/$', views.save_livestock_form, name = 'save_livestock_form'),
]