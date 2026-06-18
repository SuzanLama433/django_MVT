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

def show(request):
    data = Student.objects.all()
    return render(request,'show.html',{'sujan':data})

def count(request):
    count=0
    if request.method == "POST":
        text = request.POST['text']
        count = len(text.split())

    return render(request, 'count.html', {'count': count})

def simple(request):
    amount=0
    rate=0
    time=0
    si=0
    if request.method == "POST":
        amount = float(request.POST['amount'])
        rate = float(request.POST['rate']) 
        time = float(request.POST['time'])
        
        si = (amount*rate*time)/100
    return render(request,'simple.html',{'si':si})