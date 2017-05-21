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
    project_name = models.CharField(max_length=64)
    project_description = models.CharField(max_length=512)
    project_color = ColorField(default='#9900FF')
    project_created = models.DateField()
    project_modified = models.DateField()
    project_created_by = models.IntegerField(default=1)
    project_modified_by = models.IntegerField(default=1)
    is_active = models.BooleanField(default=False)
    client_id = models.ForeignKey('Client', db_column='client_id', default=1, on_delete=models.CASCADE)

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
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'activity'



# ======================================================


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=64)
    client_created = models.DateField()
    client_modified = models.DateField()
    client_created_by = models.IntegerField(default=1)
    client_modified_by = models.IntegerField(default=1)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'client'