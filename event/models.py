from django.db import models
import uuid

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='organizations')
    uuid = models.UUIDField(unique=True, editable=False,primary_key=True, default=uuid.uuid4)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Organization'
        ordering = ['name']