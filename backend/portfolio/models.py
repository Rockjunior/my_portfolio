from django.db import models

class AcademicExperience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class SWEExperience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()