from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Request
from .forms import RequestForm
from django.core.mail import send_mail

def request_blood(request):
    submitted = False
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            donor = form.save()
            email = request.POST.get("email")
            subject = 'You have successfully requested for Blood'
            message = 'You have successfully requested for blood. We will send you an email if the blood request gets approved or rejected.'
            send_mail(subject, message, email, [settings.EMAIL_HOST_USER, email])
            context = {'form': form, 'submitted': True}
            return render(request, 'request.html', context)
    else:
        form = RequestForm()
        if 'submitted' in request.GET:
            submitted = True
    context = {'submitted': submitted,'form': form,}
    return render(request, 'request.html', context)

def requestsforblooddetails(request):
    detail2 = Request.objects.all()
    return render(request, 'bloodrequests.html', {'detail': detail2})


