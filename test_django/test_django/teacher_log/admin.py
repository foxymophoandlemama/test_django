'''
Created on Sep 2, 2013

@author: davide
'''
from django.contrib import admin
from models import Scholar

class ScholarAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'birthdate']
    list_filter = ['grade']
    search_fields = ['surname']
    
admin.site.register(Scholar, ScholarAdmin)