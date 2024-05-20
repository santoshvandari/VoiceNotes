from django.shortcuts import render

# Create your views here.
def Home(request):
    # return HttpResponse("Hello World")
    return render(request,'Home/index.html')