from django.db import models

# Create your models here.
class UserPermissions(models.Model):
    userRole_id = models.CharField(max_length=200)
    systemPermission_id = models.CharField(max_length=200)
    isActive = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
#    created_at = models.DateTimeField('date published')