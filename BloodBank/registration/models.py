from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from storage.models import Request
import datetime
from django.urls import reverse


class DonarDetail(models.Model):
    Male = 'Male'
    Female = 'Female'
    choice = (('Male', 'Male'),
              ('Female', 'Female'),
              )
    choice1 = (('O Positive', 'O Positive'),
               ('O Negative', 'O Negative'),
               ('A Positive', 'A Positive'),
               ('A Negative', 'A Negative'),
               ('B Positive', 'B Positive'),
               ('B Negative', 'B Negative'),
               ('AB Negative', 'AB Negative'),
               ('AB Positive', 'AB Positive'),
               )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    # id_no = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=20, choices=choice, default='Male')
    age = models.IntegerField(validators=[MinValueValidator(18)])
    blood_group = models.CharField(max_length=20, choices=choice1, default='O Positive')
    email = models.EmailField()
    street = models.CharField(max_length=20, verbose_name='Address 1')
    street1 = models.CharField(max_length=40, verbose_name="Address 2")
    city = models.CharField(max_length=20, verbose_name="City")
    state = models.CharField(max_length=2, verbose_name="State")
    zipcode = models.IntegerField(validators=[MinValueValidator(5)])
    registered_by = models.CharField(max_length=20, default='Admin')
    contact_number = models.CharField(max_length=10, default=' ', null=True, blank=True)
    last_donated_date = models.DateField()
    number_month = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('donorlist')

    def refresh(self):
        now = datetime.datetime.now()
        last = self.last_donated_date
        if last != "0" or last != 0 and len(last) > 4:
            y, m, d = str(last).split('-')
            if int(d) == 0:
                self.number_month = 0
            else:
                k = datetime.datetime(int(y), int(m), int(d))
                month1 = now.year
                month2 = k.year
                if now.year == k.year:
                    if now.month != k.month:
                        m2 = now.month - k.month
                        if now.day >= k.day:
                            self.number_month = m2 + 1
                        else:
                            self.number_month = m2
                    else:
                        self.number_month = 0
                if now.year > k.year:
                    m2 = 12*(month1 - month2) - k.month + now.month
                    if now.day >= k.day:
                        self.number_month = m2 + 1
                    else:
                        self.number_month = m2
        else:
            self.number_month = -1


class Record(models.Model):
    choice1 = (('O Positive', 'O Positive'),
               ('O Negative', 'O Negative'),
               ('A Positive', 'A Positive'),
               ('A Negative', 'A Negative'),
               ('B Positive', 'B Positive'),
               ('B Negative', 'B Negative'),
               ('AB Negative', 'AB Negative'),
               ('AB Positive', 'AB Positive'),
               )
    blood_TYPE = models.CharField(max_length=20, choices=choice1, default='O Positive')
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    donar = models.ForeignKey(DonarDetail, related_name='donar_id', on_delete=models.CASCADE)
    units = models.FloatField(default=0, validators=[MinValueValidator(0)])
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    # def __str__(self):
    #     return self.id_no


class BloodStorage(models.Model):
    choice1 = (('O Positive', 'O Positive'),
               ('O Negative', 'O Negative'),
               ('A Positive', 'A Positive'),
               ('A Negative', 'A Negative'),
               ('B Positive', 'B Positive'),
               ('B Negative', 'B Negative'),
               ('AB Negative', 'AB Negative'),
               ('AB Positive', 'AB Positive'),
               )
    blood_group = models.CharField(max_length=20, choices=choice1, default='O Positive')
    units = models.FloatField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['-units']

    def __str__(self):
        return self.blood_group

    def get_absolute_url(self):
        return reverse('bloodstoragedetails')