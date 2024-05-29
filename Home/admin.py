from django.contrib import admin
from Home.models import Contact,UserNotes

# Register your models here.

# Defining the List to Display of Contact
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','message','created_at']

admin.site.register(Contact,ContactAdmin)

# Defining the List to Display of UserNotes
class UserNotesAdmin(admin.ModelAdmin):
    list_display=['user','title','note','created_at','updated_at']

admin.site.register(UserNotes,UserNotesAdmin)



