from django.db import models

# Create your models here.
class Cities(models.Model):
    country_id = models.CharField(max_length=200)
    fullName = models.CharField(max_length=200)
    PhoneCode = models.CharField(max_length=200)
    PostalCode = models.CharField(max_length=200)
    isActive = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)