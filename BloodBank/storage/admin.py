from django.contrib import admin
from .models import Request

@admin.register(Request)
class DonarDetailAdmin(admin.ModelAdmin):
    list_display = ['name','name_of_hospital', 'blood_type', 'units', 'contact_number']
    list_filter = ['name_of_hospital', 'blood_type', 'units']
    search_fields = ['name_of_hospital', 'blood_type']
    ordering = ['blood_type']
