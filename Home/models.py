from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=60, blank=False, null=False, default='Unknown')
    email=models.EmailField(max_length=100, blank=False, null=False)
    message=models.TextField(blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'
    


