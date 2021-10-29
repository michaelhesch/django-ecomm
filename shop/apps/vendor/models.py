from django.contrib.auth.models import User
from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)
    
    # Set default sorting to be done by name and not pk
    class Meta:
        ordering = ['name']

    # Return the name instead of object ID in admin, etc.
    def __str__(self):
        return self.name
