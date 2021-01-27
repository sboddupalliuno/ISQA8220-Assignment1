from django.conf.urls import url
from django.urls import path
from .views import user_logout, PasswordResetConfirmView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^logout/', user_logout),
    path('reset_confirmation/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='reset_password_confirmation'),
]