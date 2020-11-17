from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserProfile
        fields = ('username', 'email', 'department', 'employee_cell_phone')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'department', 'employee_cell_phone')

class CustomPasswordResetForm(PasswordResetForm):

    class Meta:
        model = UserProfile
        fields = ('email')