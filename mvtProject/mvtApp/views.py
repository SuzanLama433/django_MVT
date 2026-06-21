from django.shortcuts import render
from .models import Student ,Signup
from django.http import HttpResponse
import random

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

def calulator(request):
    num1=0
    num2=0
    result =0
    if request.method == "POST":
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        op = request.POST['operator']
        result =0
        if op =="+":
            result = num1+num2
        elif op == "-":
            result =num1-num2
        elif op == "*":
            result = num1 *num2
        elif op == "/":
            if num2 == 0:
                result= "cannot divided by zero"
            else :
                result =num1/num2
    return render(request,'calculator.html' ,{'result':result})

def atm(request):
    result = ""
    balance = 10000
    MyPin = "1234"
    if request.method == "POST":
        pin1 = request.POST['pin']
        option = request.POST['option']
        amount = request.POST['amount']
        
        if pin1 == MyPin:
            if option == 'balance':
                result = f'your totatl balance Rs {balance}'
            elif option == "withdraw":
                amount = int(amount)

                if amount <= balance:
                    balance -= amount
                    result = f"Withdraw successful. Remaining balance: Rs. {balance}"
                else:
                    result = "Insufficient Balance"
                    
            elif option == "deposit":
                amount = int(amount)
                balance += amount
                result = f"Deposit successful. New balance: Rs. {balance}"
        else:
            result ='invalid pin'
                
    return render(request,'atm.html' ,{'result':result})

# spr game 
def index(request):
    return render(request,'index.html')


def game(request):
    user_input = ""
    computer = ""
    result = ""

    if request.method == "POST":
        user_input = request.POST.get("words", "")  
        user_input = user_input.upper() if user_input else ""  

        computer = random.choice(["R", "P", "S"])

        if user_input not in ["R", "P", "S"]:
            result = "Invalid Input ❌"

        elif (user_input == "S" and computer == "P") or \
             (user_input == "P" and computer == "R") or \
             (user_input == "R" and computer == "S"):
            result = "You Win 🎉"

        elif user_input == computer:
            result = "Draw 😐"

        else:
            result = "Computer Wins 🤖"

    return render(request, "game.html", {
        "user": user_input,
        "computer": computer,
        "result": result
    })
    
def signup(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user = Signup(firstname=firstname, lastname=lastname,email=email,password=password, cpassword=cpassword)
        user.save()
        return HttpResponse('form is submitted..')
    return render(request,'signup.html')