from django.db import models
from student.models import Student
from course.models import Course

from django.utils.timezone import now

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(default=now)
    status = models.BooleanField()
