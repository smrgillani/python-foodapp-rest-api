from django.db import models

# Create your models here.
class Countries(models.Model):
    currency_id = models.CharField(max_length=200)
    fullName = models.CharField(max_length=200)
    ISO = models.CharField(max_length=200)
    PhoneCode = models.CharField(max_length=200)
    isActive = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
    # updated_at = models.DateTimeField('date published')
    # created_at = models.DateTimeField('date published')