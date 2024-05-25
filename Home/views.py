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


def ContactUs(request):
    if request.method == 'POST':
        name = (request.POST['fullname']).strip()
        email = (request.POST['email']).strip()
        message = (request.POST['message']).strip()
        if name and email and message:
            try:
                contact=Contact(name=name,email=email,message=message)
                contact.save()
                return render(request,'Home/contact.html',{'success':'Thank you for contacting us. We will get back to you soon.'})
            except Exception as e:
                print(e)
                return render(request,'Home/contact.html',{'error':' * Something went wrong. Please try again later.'})
        else:
            return render(request,'Home/contact.html',{'error':' * Please fill all the fields.'})
    return render(request,'Home/contact.html')