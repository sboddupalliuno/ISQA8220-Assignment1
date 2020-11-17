from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    department = models.CharField(max_length=50, default=' ', null=True, blank=True)
    employee_cell_phone = models.CharField(max_length=10, default=' ', null=True, blank=True)

