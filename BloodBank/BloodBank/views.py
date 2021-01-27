from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from users.models import UserProfile
from registration.models import BloodStorage, DonarDetail
from django.contrib.auth import views as auth_views, forms as auth_forms
from django.views.generic.edit import UpdateView, DeleteView

class ChangePasswordResetDoneView(auth_views.PasswordChangeView):
    form_class = auth_forms.PasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('change_password_done')

class ChangePasswordResetDoneSuccessView(auth_views.PasswordChangeView):
    form_class = auth_forms.PasswordChangeForm
    template_name = 'change_password_done.html'

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
    success_url = reverse_lazy('reset_password_complete')

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    form_class = auth_forms.PasswordResetForm
    template_name = 'reset_password_complete.html'
    #success_url = reverse_lazy('login.html')

