from django.db import models

# Create your models here.
class Users(models.Model):
    u_id = models.AutoField(primary_key=True)
    unq_id = models.CharField(max_length=255)
    contact_id = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    emailAddr = models.CharField(max_length=200)
    userRole_id = models.CharField(max_length=200)
    isActive = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
#    created_at = models.DateTimeField('date published')