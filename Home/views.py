from django.shortcuts import render

# Create your views here.
def Home(request):
    # return HttpResponse("Hello World")
    return render(request,'Home/index.html')
def PrivacyPolicy(request):
    return render(request,'Home/privacypolicy.html')


def About(request):
    return render(request,'Home/about.html')


def Contact(request):
    return render(request,'Home/contact.html')