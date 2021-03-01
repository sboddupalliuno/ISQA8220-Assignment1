"""BloodBank URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url, include
from .views import ChangePasswordResetDoneSuccessView, ChangePasswordResetDoneView,PasswordResetView, DonorUpdateView, donorlist, \
    PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView, BloodAvailableUpdateView, BloodAvailableDeleteView, blood_storage

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    url(r'^storage/', include('storage.urls')),
    url(r'^register/', include('users.urls'), name='staffregister'),
    path('reset_password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset_password/done/', PasswordResetDoneView.as_view(), name='reset_password_done'),
    path('reset_confirmation/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='reset_password_confirmation'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='reset_password_complete'),
    path('password_change/', ChangePasswordResetDoneView.as_view(), name='password_change'),
    path('change_password_done/', ChangePasswordResetDoneSuccessView.as_view(), name='change_password_done'),
    path('<int:pk>/edit/',BloodAvailableUpdateView.as_view(), name='bloodstorage_edit'),
    path('<int:pk>/delete/',BloodAvailableDeleteView.as_view(), name='bloodstorage_delete'),
    url(r'^bloodstoragedetails/', blood_storage, name='bloodstoragedetails'),
    path('<int:pk>/donoredit/', DonorUpdateView.as_view(), name='donor_edit'),
    url(r'^donorlist/', donorlist, name='donorlist'),
]