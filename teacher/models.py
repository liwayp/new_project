from django.db import models
from user.models import User

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    subjects = models.CharField(max_length=255)