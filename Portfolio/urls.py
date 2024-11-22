from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("contacts/", views.contacts, name="contacts"),
    path("certificates/", views.Certificates, name="certificates"),
    
]