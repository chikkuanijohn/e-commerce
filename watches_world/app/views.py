from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
import os
from django.contrib.auth.models import User

# Create your views here.

def watches_world_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['shop']=uname 
                return redirect(shop_home)
            else:
                req.session['user']=uname 
                return redirect(user_home)
        else:
            messages.warning(req,'invalid username or password') 
            return redirect(watches_world_login)  
    else:
        return render(req,'login.html')

def watches_world_shop_logout(req):
    logout(req)
    req.session.flush() #for deleting the session
    return redirect(watches_world_login)

def shop_home(req):
    if 'shop' in req.session:
        data=Product.objects.all()
        return render(req,'shop/home.html',{'Products':data})
    else:
        return redirect(watches_world_login)

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
        except:
            messages.warning(req,'invalid username or password')
            return redirect(register)   
        return redirect(watches_world_login) 
    else:
        return render(req,'user/register.html')    
    
    
def user_home(req):
    if 'user' in req.session:
        data=Product.objects.all()
        return render(req,'user/user_home.html',{'Products':data})
    else:
        return redirect(watches_world_login)
