from django.contrib import admin
from .models import DonarDetail, Record, BloodStorage


@admin.register(DonarDetail)
class DonarDetailAdmin(admin.ModelAdmin):
    list_display = ['id_no','first_name', 'last_name', 'gender', 'blood_group', 'contact_number', 'last_donated_date']
    list_filter = ['blood_group', 'id_no', 'first_name','last_name']
    search_fields = ['blood_group','id_no']
    ordering = ['blood_group']

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['blood_TYPE', 'staff', 'id_no', 'donar_name', 'units', 'date']
    list_filter = ['blood_TYPE', 'units', 'donar_name']
    search_fields = ['blood_TYPE', 'units']
    ordering = ['blood_TYPE']

@admin.register(BloodStorage)
class BloodStorageAdmin(admin.ModelAdmin):
    list_display = ['blood_group', 'units' ]
    list_filter = ['blood_group']
    search_fields = ['blood_group']
    ordering = ['blood_group']