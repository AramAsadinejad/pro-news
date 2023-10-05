from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_user(request):
    if request.method=='POST':
        
        user_username=request.POST["username"]
        user_password=request.POST["password"]
        user=authenticate(request,username=user_username,password=user_password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.success(request,"wrong username or password")
            return redirect("login")

    return render(request,"login.html",{})

def logout_user(request):
    logout(request)
    return redirect("home")

def register(request):
    if request.method=="POST":
        myform=UserCreationForm(request.POST)
        if myform.is_valid():
            myform.save()
            messages.success(request,'u registerd!')
            return redirect('login')
        else:
            messages.success(request,'something went wrong')
            return redirect("register")
    myform=UserCreationForm()
    return render(request,"register.html",{
        "myform":myform,
    })