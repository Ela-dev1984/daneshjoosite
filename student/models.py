from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    average = models.FloatField(default=0)
    bio = models.TextField(max_length=100)
