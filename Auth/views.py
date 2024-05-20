from django.shortcuts import render
from django.contrib.auth import logout,login


# Create your views here.
def log_in(request):
    if request.method == 'POST':
        pass
    return render(request,'Auth/login.html')

def register(request):
    if request.method == 'POST':
        pass
    return render(request,'Auth/register.html')

def log_out(request):
    logout(request)

