from django.db import models


class Employee(models.Model):
    employee_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    disabled = models.BooleanField(default = False)

    class Meta:
        db_table = 'employee'
