from django.shortcuts import render,redirect
from Home.models import Contact,UserNotes

# Create your views here.
# Completed 
def Home(request):
    if request.method == 'POST':
        notetitle = (request.POST['NoteTitle']).strip()
        notebody = (request.POST['NoteContent']).strip()
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


# Completed 
def PrivacyPolicy(request):
    return render(request,'Home/privacypolicy.html')


# Completed
def About(request):
    return render(request,'Home/about.html')


# Completed 
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



# Completed
def MyNotes(request):
    if not request.user.is_authenticated:
        return redirect('/404')
    try:
        usernotes = UserNotes.objects.filter(user=request.user)
        if usernotes:
            return render(request,'Home/mynotes.html',{'notes':usernotes})
        else:
            return render(request,'Home/mynotes.html',{'error':'No Records Found.'})
    except Exception as ex:
        print(ex)
        return render(request,'Home/mynotes.html',{'error':'Something went wrong. Please try again later.'})
    return render(request,'Home/mynotes.html')



# Completed Too

def SingleNotes(request,id):
    if not request.user.is_authenticated:
        return redirect('/404')
    if not id:
        return redirect('/404')


    if request.method == 'POST':
        notetitle = (request.POST['NoteTitle']).strip()
        notebody = (request.POST['NoteContent']).strip()
        if notetitle and notebody:
            try:
                usernotes = UserNotes.objects.get(user=request.user,id=id)
                if not usernotes:
                    return redirect('/404')
                usernotes.title = notetitle
                usernotes.note = notebody
                usernotes.save()
                return render(request,'Home/index.html',{'success':'Note Updated successfully.'})
            except Exception as e:
                data={
                    'notetitle':notetitle,
                    'notecontent':notebody,
                    'error':'* Failed to Update Note. Please try again later.'
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

    if id:
        try:
            usernotes = UserNotes.objects.get(user=request.user,id=id)
            if usernotes:
                usernote={
                    'title':usernotes.title,
                    'note':usernotes.note
                }
                return render(request,'Home/SingleNotesView.html',usernote)
            else:
                return redirect('/404')
        except Exception as ex:
            print(ex)
            return redirect("/404")

    # usernotes=UserNotes(user=request.user,title=notetitle,note=notebody)
    #             usernotes.save()
    #             return render(request,'Home/index.html',{'success':'Note saved successfully.'})
    return redirect("/404")





# Code Completed
def NotesDelete(request,id):
    # Check the user is authenticated or not
    if not request.user.is_authenticated:
        return redirect('/404')
    if not id:
        return redirect('/404')
    if id:
        try:
            usernotes = UserNotes.objects.get(user=request.user,id=id)
            if usernotes:
                usernotes.delete()
                return redirect('/mynotes')
            else:
                return redirect('/404')
        except Exception as ex:
            print(ex)
            return redirect('/404')




# Custom 404 Page
def Custom404(request):
    return render(request,"Home/404.html")
