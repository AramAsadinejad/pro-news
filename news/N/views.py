from django.shortcuts import render,redirect
from .models import news
from .forms import NewsForm
from django.contrib import messages

def home(request):
    posts=news.objects.all()
    return render(request,"home.html",{
        "posts":posts,
    })

def delete(request,news_id):
    if request.user.is_superuser:
        mypost=news.objects.get(pk=news_id)
        mypost.delete()
    return redirect("home")

def update(request,news_id):
    mypost=news.objects.get(pk=news_id)
    if request.user.is_superuser:
        if request.method=='POST':
            myform=NewsForm(request.POST,request.FILES)
            if myform.is_valid():
                delete(request,news_id)
                myform.save()
                return redirect("home")    
        else:
            mypost=news.objects.get(pk=news_id)
            if request.user.is_superuser:
                myform=NewsForm(request.POST or None,instance=mypost)
                if myform.is_valid():
                    myform.save()
                    return redirect("home")
    return render(request,'update.html',{
        "myform":myform
    })

def create(request):
        if request.user.is_superuser:
            if request.method=="POST":
                myform2=NewsForm(request.POST,request.FILES)
                if myform2.is_valid():
                    myform2.save()
                    messages.success(request,"your post added successfully")
                    return redirect("home")
                else:
                    messages.success(request,"error")
                    return redirect("home")

            else:
                myform=NewsForm
        return render(request,"create.html",{
                "myform":myform,
                
        })