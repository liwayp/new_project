from django.db import models
from student.models import Student
from teacher.models import Teacher

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
