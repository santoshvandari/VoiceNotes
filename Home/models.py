from django.db import models
from django.db.models import User


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=60, blank=False, null=False, default='Unknown')
    email=models.EmailField(max_length=100, blank=False, null=False)
    message=models.TextField(blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'
    

class UserNotes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.TextField(blank=False, null=False)
    note=models.TextField(blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='User Note'
        verbose_name_plural='User Notes'
