from django import forms
from rest_framework import serializers
from .models import Record, DonarDetail

class DateInput(forms.DateInput):
    input_type = 'date'


class DonateForm(forms.ModelForm):
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
        model = Record
        fields = ('blood_group', 'donar', 'units', 'date')
        widgets = {
            'date': DateInput()
        }

class DonarForm(forms.ModelForm):
    class Meta:
        model = DonarDetail
        fields = ('first_name', 'last_name', 'gender', 'age', 'blood_group',
                  'email', 'street', 'street1', 'city', 'state', 'zipcode', 'contact_number',
                  'last_donated_date')
        widgets = {
            'last_donated_date': DateInput()
        }