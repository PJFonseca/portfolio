from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ects = models.IntegerField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

class Discipline(models.Model):
    # One Discipline exists in one course, I'm assuming every discipline is tailored for that course only
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200)
    description = models.TextField()
    ects = models.IntegerField()
    background_color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

