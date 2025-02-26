from django.db import models
from student.models import Student
from course.models import Course
from django.utils.timezone import now

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.IntegerField(max_length=10)
    date_assigned = models.DateTimeField(default=now)