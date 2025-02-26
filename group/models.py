from django.db import models
from teacher.models import Teacher 
from course.models import Course
from django.utils.timezone import now

class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room = models.CharField(max_length=255)
    started_at = models.DateTimeField(default=now)
    subject = models.CharField(max_length=255)
    sb_code = models.IntegerField(unique = True)
