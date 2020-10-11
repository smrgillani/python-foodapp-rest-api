from django.db import models

# Create your models here.
class Currencies(models.Model):
    fullName = models.CharField(max_length=200)
    Sign = models.CharField(max_length=200)
    isActive = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)