from django.shortcuts import render
from .models import Contact

def home(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact=Contact(fullname=name,email=email,subject=subject,message=message)
        contact.save()
    return render(request,'index.html')

def about(request):
    return render(request,'aboutme.html')

