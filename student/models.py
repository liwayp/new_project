from django.db import models
from user.models import User
from django.utils.timezone import now


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    enrollment_date = models.DateTimeField(default=now)
    address = models.CharField(max_length=55)