from django.contrib import admin
from Home.models import Contact

# Register your models here.

# Defining the List to Display
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','message','created_at']




admin.site.register(Contact,ContactAdmin)
