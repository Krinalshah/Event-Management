from django.db import models

# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Users'
        ordering = ['email']


# class Event(models.Model):
#     name = models.CharField(max_length=255)
#     date = models.DateTimeField()
#     location = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name



