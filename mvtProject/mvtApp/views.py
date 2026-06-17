from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method == "POST":
        data = request.POST
        nm = data['name']
        age = data['age']
        email = data['email']
        message = data['message']
        
        user = Student(name=nm,age=age,email=email,message=message) 
        user.save()
        return HttpResponse("your message is submitted.....")
    return render(request,'home.html')