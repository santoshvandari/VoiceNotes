from django.urls import path
from Home import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('home/',views.Home,name='home'),    
    path('about/',views.About,name='about'),
    path('contact/',views.Contact,name='contact'),
    path('privacypolicy/',views.Login,name='privacypolicy'),
]
