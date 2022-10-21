from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    class_room = models.CharField(max_length=3)
    age = models.IntegerField()
