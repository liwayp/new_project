from django.db import models
from django.utils.timezone import now

class Lead(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)