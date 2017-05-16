import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# ======================================================


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



# ======================================================


class Event(models.Model):
    event_id = models.AutoField(primary_key = True)
    start = models.DateTimeField('Event start date & time')
    end = models.DateTimeField('Event end date & time')
    employee_id = models.IntegerField(default = 0)
    project_id = models.IntegerField(default = 0)