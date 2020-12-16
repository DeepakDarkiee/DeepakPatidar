from django.contrib import admin
from .models import Contact
from django.apps import apps



class ContactAdmin(admin.ModelAdmin):
    list_display = ('fullname','email','subject','created_on')
admin.site.register(Contact, ContactAdmin)