from django.shortcuts import render,redirect
from django.contrib.auth import logout,login
from django.contrib.auth.models import User


# Create your views here.
def log_in(request):
    if request.method == 'POST':
        username=request.POST['username'].strip()
        password=request.POST['password']
        if username=='' or password=='':
            return render(request,'Auth/login.html',{'error':'* All Fields are required'})
        user=User.objects.filter(username=username).first()
        if user is not None:
            if user.check_password(password):
                login(request,user)
                return redirect('home')
            else:
                return render(request,'Auth/login.html',{'error':'* Invalid Password'})
        else:
            return render(request,'Auth/login.html',{'error':'* Invalid Username'})
    return render(request,'Auth/login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username'].strip()
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        firstname=request.POST['firstname'].strip()
        lastname=request.POST['lastname'].strip()
        email=request.POST['email'].strip()
        if username=='' or password=='' or confirm_password=='' or firstname=='' or lastname=='' or email=='':
            return render(request,'Auth/register.html',{'error':'* All Fields are required'})
        if password!=confirm_password:
            return render(request,'Auth/register.html',{'error':'* Passwords do not match'})
        if User.objects.filter(username=username).exists():
            return render(request,'Auth/register.html',{'error':'* Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request,'Auth/register.html',{'error':'* Email already exists'})
        try:
            user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
            user.save()
            login(request,user)
            return redirect('home')
        except:
            return render(request,'Auth/register.html',{'error':'* An error occurred'})
        

    return render(request,'Auth/register.html')

def log_out(request):
    logout(request)
    return redirect('login')

