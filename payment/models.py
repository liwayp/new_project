from django.db import models
from student.models import Student
from group.models import Group 
from django.utils.timezone import now

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default = False)
    date_paid = models.DateTimeField(default = now)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)