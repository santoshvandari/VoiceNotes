from django.shortcuts import render,HttpResponse
from Home.models import Contact,UserNotes

# Create your views here.
def Home(request):
    if request.method == 'POST':
        notetitle = (request.POST['NoteTitle']).strip()
        notebody = (request.POST['NoteContent']).strip()
        print(notetitle,notebody)
        if notetitle and notebody:
            try:
                usernotes=UserNotes(user=request.user,title=notetitle,note=notebody)
                usernotes.save()
                return render(request,'Home/index.html',{'success':'Note saved successfully.'})
            except Exception as e:
                data={
                    'notetitle':notetitle,
                    'notecontent':notebody,
                    'error':'* Something went wrong. Please try again later.'
                }
                print(e)
                return render(request,'Home/index.html',data)
        else:
            data={
                'notetitle':notetitle,
                'notecontent':notebody,
                'error':'* Please fill all the fields.'
            }
            return render(request,'Home/index.html',data)
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

def MyNotes(request):
    return render(request,'Home/mynotes.html')

def SingleNotes(request,id):
    if not id:
        return redner(request,"Home/404.html")
    if not id.isDigit():
    	return render(request,"Home/404.html")



    # usernotes = UserNotes. 

    # usernotes=UserNotes(user=request.user,title=notetitle,note=notebody)
    #             usernotes.save()
    #             return render(request,'Home/index.html',{'success':'Note saved successfully.'})
    return render(request,"Home/SingleNotesView.html")
