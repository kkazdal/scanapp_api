from django.db import models

# Create your models here.

class Task(models.Model):
  photo = models.ImageField(upload_to='media/photo/')
