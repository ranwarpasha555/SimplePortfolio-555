from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


# Create your views here.
# Anwar@555 and FirdoseBegum@786


def index(request):
  return render(request,'index.html')

def contacts(request):
  if request.method =="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email',' ')
        number=request.POST.get('number',' ')  
        date = request.POST.get('date',' ') 
        desc=request.POST.get('desc',' ')
        contact = Contact(name=name, email=email, number = number,date = date, desc=desc)
        contact.save()
        return HttpResponse("Thank you for your message.....!👍👍👍 ")
        
  return render(request, "contacts.html")
  

def Certificates(request):
  return render(request,'certificates.html')
