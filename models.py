from django.db import models

# Create your models here.

class LogEntry(models.Model):
    message = models.CharField(max_length=255)