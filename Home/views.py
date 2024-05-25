from django.shortcuts import render
from Home.models import Contact

# Create your views here.
def Home(request):
    # return HttpResponse("Hello World")
    return render(request,'Home/index.html')
def PrivacyPolicy(request):
    return render(request,'Home/privacypolicy.html')


def About(request):
    return render(request,'Home/about.html')


def Contact(request):
    if request.method == 'POST':
        name = (request.POST['name']).strip()
        email = (request.POST['email']).strip()
        message = (request.POST['message']).strip()
        if name and email and message:
            

    return render(request,'Home/contact.html')