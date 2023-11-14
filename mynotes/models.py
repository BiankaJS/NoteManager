import datetime
from django.utils import timezone
from django.db import models

class Note(models.Model): 
  title = models.CharField(max_length=1000)
  content = models.TextField()
  creation_date = models.DateTimeField("creation_date")
  id = models.AutoField(primary_key=True)

  def __str__(self):
    return self.title