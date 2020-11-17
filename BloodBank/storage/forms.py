from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    choice1 = (('O Positive', 'O Positive'),
               ('O Negative', 'O Negative'),
               ('A Positive', 'A Positive'),
               ('A Negative', 'A Negative'),
               ('B Positive', 'B Positive'),
               ('B Negative', 'B Negative'),
               ('AB Negative', 'AB Negative'),
               ('AB Positive', 'AB Positive'),
               )
    blood_group = forms.ChoiceField(choices=choice1, initial='O Positive')

    class Meta:
        model = Request
        fields = ('name', 'name_of_hospital', 'blood_group', 'units', 'reason','email', 'contact_number')