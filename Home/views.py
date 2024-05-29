from django.shortcuts import render
from Home.models import Contact

# Create your views here.
def Home(request):
    # return HttpResponse("Hello World")
    if request.method == 'POST':
        notetitle = (request.POST['NoteTitle']).strip()
        notebody = (request.POST['notebody']).strip()
        if notetitle and notebody:
            try:
                usernotes=UserNotes(user=request.user,title=notetitle,note=notebody)
                usernotes.save()
                return render(request,'Home/index.html',{'success':'Note saved successfully.'})
            except Exception as e:
                print(e)
                return render(request,'Home/index.html',{'error':' * Something went wrong. Please try again later.'})
        else:
            return render(request,'Home/index.html',{'error':' * Please fill all the fields.'})
            
    data ="Lorem ipsum dolor, sit amet consectetur adipisicing elit. Non optio, similique eveniet a ipsa deleniti facere ipsum veritatis deserunt rerum. Dolorem suscipit aspernatur repudiandae cumque veritatis nobis earum pariatur magnam!"
    return render(request,'Home/index.html',{'data':data})
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