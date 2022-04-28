from django.db import models
import datetime

# Create your models here.
class Todo(models.Model):
     title=models.CharField(max_length=200)
     day=models.DateField(default=datetime.date.today)
     complete=models.BooleanField(default=False)

     def __str__(self):
          return self.title







