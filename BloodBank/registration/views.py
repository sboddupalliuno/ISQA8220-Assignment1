from io import BytesIO
from django.shortcuts import redirect
from xhtml2pdf import pisa
from django.conf import settings
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic.edit import UpdateView, DeleteView
from .models import DonarDetail, Record, BloodStorage
from .forms import DonateForm, DonarForm
from datetime import datetime, timedelta
from django.urls import reverse_lazy

def add_donar(request):
    submitted = False
    error = []
    if request.method == 'POST':
        form = DonarForm(request.POST)
        if "last_donated_date" not in request.POST:
            error.append('Provide Last Donated Date')
        if "last_donated_date" in request.POST:
            lastDonatedDate = request.POST.get("last_donated_date")
            todaysDate = datetime.now().date()
            lastDate = datetime.strptime(lastDonatedDate, '%Y-%m-%d').date()
            if lastDate > todaysDate:
                error.append('Provide Last Donated Date in the past')
        if len(error) != 0:
            context = {'form': form, 'submitted': True, 'errors': error}
            return render(request, 'login/donnarform.html', context)
        if form.is_valid():
            donor = form.save(commit=False)
            lastDonatedDate = request.POST.get("last_donated_date")
            todaysDate = datetime.now().date()
            lastDate = datetime.strptime(lastDonatedDate , '%Y-%m-%d').date()
            num_months = (todaysDate.year - lastDate.year) * 12 + (todaysDate.month - lastDate.month)
            donor.number_month = num_months
            donor = form.save()
            email = request.POST.get("email")
            subject = 'You have successfully registered'
            message = 'You have successfully registered for blood donation. Thank you for choosing to donate blood.'
            send_mail(subject, message, email, [settings.EMAIL_HOST_USER, email])
            context = {'form': form, 'submitted': True}
            return render(request, 'donorform.html', context)
    else:
        form = DonarForm()
        if 'submitted' in request.GET:
            submitted = True
    context = {'submitted': submitted,'form': form,}
    return render(request, 'donorform.html', context)


def donate(request):
    error = []
    if request.method == 'POST':
        record = Record()
        record.blood_TYPE = request.POST['blood_group']
        if int(request.POST['units']) > 2:
            error.append('Cannot more than 2 units')
        if DonarDetail.objects.all().filter(id=str(request.POST['donar']).upper()):
            if DonarDetail.objects.all().filter(id=str(request.POST['donar']).upper(),blood_group=record.blood_TYPE,):
                donorDetail = DonarDetail.objects.get(id=request.POST['donar'])
                todaysDate = datetime.now().date()
                lastDate = donorDetail.last_donated_date
                num_months = (todaysDate.year - lastDate.year) * 12 + (todaysDate.month - lastDate.month)
                print(lastDate)
                print(todaysDate)
                print((todaysDate.year - lastDate.year) * 12 + (todaysDate.month - lastDate.month))
                print(num_months)
                if num_months >= 3:
                    print('ok')
                else:
                    error.append('donor not eligible')
            else:
                error.append('blood does not match donor ')
        else:
            error.append('donor not available ')
        if len(error) == 0:
            donorDetail = DonarDetail.objects.get(id=request.POST['donar'])
            record = Record.objects.create(donar=donorDetail,
                                           blood_TYPE=request.POST['blood_group'],
                                           units=request.POST['units'],
                                           date=datetime.strptime(request.POST['date'], '%Y-%m-%d').date(),
                                           user_id=request.user.id)
            record.save()
        else:
            form = DonateForm()
            return render(request, 'donate.html', {'form': form, 'errors': error})
        a = DonarDetail.objects.get(id=str(request.POST['donar']).upper())
        a.last_donated_date = request.POST['date']
        a.refresh()
        a.save()
        storage = BloodStorage()
        if BloodStorage.objects.all().filter(blood_group=request.POST['blood_group']):
            storage1 = BloodStorage.objects.get(blood_group=request.POST['blood_group'])
            storage1.units += float(request.POST['units'])
            storage1.save()
        else:
            storage.blood_group = request.POST['blood_group']
            storage.units = request.POST['units']
            storage.save()
        form = DonarForm()
        context = {'submitted': True, 'form': form, }
        return render(request, 'donate.html', context)
    else:
        error = []
        form = DonateForm()
        return render(request, 'donate.html', {'form': form, 'error': error})


def blood_storage(request):
    detail1 = BloodStorage.objects.all()
    return render(request, 'blood.html', {'detail': detail1})


def records(request):
    detail2 = Record.objects.all()
    return render(request, 'records.html', {'detail': detail2})

def donordetails(request):
    detail2 = DonarDetail.objects.all()
    return render(request, 'donordetails.html', {'detail': detail2})

def sendpdfEmail(request):
    detail1 = Record.objects.all()
    context = {'detail':detail1}
    pdfbytes = render_to_pdf('bloodemail.html', context)
    if pdfbytes:
        email= request.user.email
        subject = "Blood Records"
        from_email = settings.EMAIL_HOST_USER
        email = EmailMultiAlternatives(subject=subject, body="The List of Blood Records", from_email=from_email, to=[email])
        email.attach(filename='BloodDonationRecords.pdf', content=pdfbytes, mimetype='application/pdf')
        email.send()
        return redirect('/records/')

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.replace(u'\ufeff', '').encode("latin-1")), result)
    if not pdf.err:
        return result.getvalue()
    return None

def sendpdfEmaildonordetails(request):
    detail1 = DonarDetail.objects.all()
    context = {'detail':detail1}
    pdfbytes = render_to_pdf('donordetailsemail.html', context)
    if pdfbytes:
        email= request.user.email
        subject = "Donor Details Records"
        from_email = settings.EMAIL_HOST_USER
        email = EmailMultiAlternatives(subject=subject, body="The List of Donors", from_email=from_email, to=[email])
        email.attach(filename='DonorRecords.pdf', content=pdfbytes, mimetype='application/pdf')
        email.send()
        return redirect('/donordetails/')

class BloodAvailableUpdateView(UpdateView):
    model = BloodStorage
    fields = ('blood_group', 'units')
    template_name = 'bloodstorage_edit.html'

class BloodAvailableDeleteView(DeleteView):
    model = BloodStorage
    template_name = 'bloodstorage_delete.html'
    success_url = reverse_lazy('home')