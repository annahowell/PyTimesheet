from django.conf import settings
from django.db import models


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    start = models.DateTimeField('Event began')
    end = models.DateTimeField('Event ended')
    project_id = models.IntegerField(default=0)

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        db_column='user_id',
        on_delete=models.CASCADE,
        default=1,
    )

    class Meta:
        db_table = 'event'


# ======================================================


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=64)
    project_description = models.CharField(max_length=512)
    project_color = models.CharField(max_length=6)
    disabled = models.BooleanField(default=False)

    class Meta:
        db_table = 'project'
