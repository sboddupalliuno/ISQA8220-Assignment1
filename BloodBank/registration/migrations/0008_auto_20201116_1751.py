# Generated by Django 2.2 on 2020-11-16 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_remove_donardetail_id_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donardetail',
            name='contact_number',
            field=models.CharField(blank=True, default=' ', max_length=10, null=True),
        ),
    ]