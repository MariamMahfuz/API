from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(default=0)
    father_name=models.CharField(max_length=35)