from django.db import models

# Create your models here.
class LocalAddresses(models.Model):
    city_id = models.CharField(max_length=200)
    fullAddress = models.CharField(max_length=200)
    isActive = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)