from django.shortcuts import render,redirect
from django.contrib.auth import logout,login
from django.contrib.auth.models import User


# Create your views here.
def log_in(request):
    if request.method == 'POST':
        username=request.POST['username'].strip()
        password=request.POST['password'].strip()
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
        pass
    return render(request,'Auth/register.html')

def log_out(request):
    logout(request)
    return redirect('login')

