from django.conf import settings
from django.db import models
from colorfield.fields import ColorField


# Employees are handled with django's User model as non-superusers
# ColorField uses https://github.com/jaredly/django-colorfield

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    start = models.DateTimeField('Event began')
    end = models.DateTimeField('Event ended')
    event_created = models.DateField()
    event_modified = models.DateField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='user_id', default=1, on_delete=models.CASCADE)
    project_id = models.ForeignKey('Project', db_column='project_id', default=1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'


# ======================================================


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField('Name', max_length=64)
    project_description = models.CharField('Description', max_length=512)
    project_color = ColorField('Color', default='#9900FF')
    project_created = models.DateField()
    project_modified = models.DateField()
    project_created_by = models.IntegerField(default=199)
    project_modified_by = models.IntegerField(default=199)
    is_active = models.BooleanField(default=True)
    client_id = models.ForeignKey('Client', db_column='client_id', default=9, on_delete=models.CASCADE)

    class Meta:
        db_table = 'project'


# ======================================================


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=64)
    activity_color = ColorField(default='#9900FF')
    activity_created = models.DateField()
    activity_modified = models.DateField()
    activity_created_by = models.IntegerField(default=1)
    activity_modified_by = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'activity'



# ======================================================


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_business_name = models.CharField('Business name', default='', max_length=64)
    client_contact_name  = models.CharField('Contact name', default='', max_length=64)
    client_phone_number = models.CharField('Telephone no', default='', max_length=32)
    client_email = models.EmailField('Email address', default='', max_length=128)
    client_address1 = models.CharField('Address', default='', max_length=128)
    client_address2 = models.CharField('Address cont', default='', max_length=128)
    client_postcode = models.CharField('Postcode', default='', max_length=32)
    client_created_on = models.DateTimeField()
    client_modified_on = models.DateTimeField()
    client_created_by = models.IntegerField(default=1)
    client_modified_by = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'client'
