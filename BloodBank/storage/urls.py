from django.conf.urls import url
from . import views

app_name = 'storage'
urlpatterns = [
    url(r'^request/$',views.request_blood, name='request'),
    url(r'^requestdetails/$',views.requestsforblooddetails, name='requestdetails'),
]