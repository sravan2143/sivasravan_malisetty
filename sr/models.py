from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  # New field to store creation time

    def __str__(self):
        return self.name
