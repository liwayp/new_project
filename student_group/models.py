from django.db import models
from student.models import Student
from group.models import Group
from django.utils.timezone import now

class StudentGroup(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    join_date = models.DateTimeField( default=now)