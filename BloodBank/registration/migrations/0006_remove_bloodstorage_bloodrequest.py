# Generated by Django 2.2 on 2020-11-13 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20201025_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodstorage',
            name='bloodrequest',
        ),
    ]