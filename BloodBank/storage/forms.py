from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('name', 'name_of_hospital', 'blood_type', 'units', 'reason','email', 'contact_number')