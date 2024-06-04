from django.urls import path
from Home import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('home/',views.Home,name='home'),    
    path('contact/',views.ContactUs,name='contact'),
    path("mynotes/",views.MyNotes,name='mynotes'),
    path("singlenotes/<int:id>",views.SingleNotes,name="singlenotes"),
    path("delete/<int:id>",views.NotesDelete,name="deletenotes"),  
    path("404/",views.Custom404,name='custom404'),
]