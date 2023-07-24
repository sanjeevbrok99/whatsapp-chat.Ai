
from django.contrib import admin

from django.urls import path,include
from apto import views

urlpatterns = [
    path("",views.homepage,name='route'),
    path("webhook",views.whatsapp_webhook,name='Whatsapp-webhook'),
    
    
]
#webhookURL-"beb061bd-ba78-4928-919e-5fc8a7f76983"
#Token-"24f8f399-97d0-4d1d-b7c1-2a5767d3ac64"
