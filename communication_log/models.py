from django.db import models
from student.models import Student
from lead.models import Lead
from django.utils.timezone import now

class CommunicationLog(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(dafault=now)

