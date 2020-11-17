from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import CustomUserCreationForm
from registration.models import DonarDetail, BloodStorage
from django.contrib.auth import views as auth_views, forms as auth_forms
from .forms import CustomUserCreationForm, CustomPasswordResetForm
from django.shortcuts import render, redirect
from django.urls import reverse

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'

def home(request):
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return redirect(reverse('home'))


def public_home(request):
    return redirect(reverse('home'))


def storage(request):
    detail1 = BloodStorage.objects.all()
    return render(request, 'blood storage.html', {'detail': detail1})

class PasswordResetView(auth_views.PasswordResetView):
    form_class = auth_forms.PasswordResetForm
    template_name = 'reset_password.html'
    email_template_name = 'reset_password_email.html'
    success_url = reverse_lazy('reset_password_done')

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    form_class = auth_forms.PasswordResetForm
    template_name = 'reset_password_done.html'
    #success_url = reverse_lazy('reset_password_done')

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    form_class = auth_forms.SetPasswordForm
    template_name = 'reset_password_confirm.html'
    success_url = reverse_lazy('reset_password_confirmation')

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    form_class = auth_forms.PasswordResetForm
    template_name = 'reset_password_complete.html'
    #success_url = reverse_lazy('login.html')
