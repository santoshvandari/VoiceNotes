from django.urls import path
from Home import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('home/',views.Home,name='home'),    
    path('about/',views.About,name='about'),
    path('contact/',views.ContactUs,name='contact'),
    path('privacypolicy/',views.PrivacyPolicy,name='privacypolicy'),
    path("mynotes/",views.MyNotes,name='mynotes'),
    path("singlenotes/<int:id>",views.SingleNotes,name="singlenotes"),
]
