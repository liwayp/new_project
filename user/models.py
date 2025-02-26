from django.db import models
role = {
    "1": "Admin",
    "2": "Teacher",
    "3": "Student",
}


class User(models.Model):
    role = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)