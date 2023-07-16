
from django.contrib import admin

from django.urls import path,include
from apto import views

urlpatterns = [
    path("",views.homepage,name='route'),
    
    
]
