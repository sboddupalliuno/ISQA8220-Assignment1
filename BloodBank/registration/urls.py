from django.conf.urls import url
from django.urls import path
from . import views
from .views import  donate, records,donordetails

app_name = 'registration'
urlpatterns = [
    # path('<int:pk>/edit/',views.BloodAvailableUpdateView.as_view(), name='bloodstorage_edit'),
    # path('<int:pk>/delete/',views.BloodAvailableDeleteView.as_view(), name='bloodstorage_delete'),
    url(r'^register/$',views.add_donar, name='register'),
    url(r'^donate/$', donate),
    url(r'^blood/', views.blood_storage, name='blood'),
    url(r'^sendpdfEmail/', views.sendpdfEmail, name='sendpdfEmail'),
    url(r'^records/', records, name='records'),
    url(r'^donordetails/', donordetails, name='donordetails'),
    url(r'^sendpdfEmaildonordetails/', views.sendpdfEmaildonordetails, name='donordetails'),
]