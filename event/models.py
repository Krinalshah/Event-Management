from django.db import models
import uuid

# Create your models here.
class Organization(models.Model):
    uuid = models.UUIDField(unique=True, editable=False,primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='organizations')
   
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Organization'
        ordering = ['name']




class Event(models.Model):
    uuid = models.UUIDField(unique=True, editable=False,primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='events')
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Event'
        ordering = ['-date', 'name']
class  Members(models.Model):
    uuid = models.UUIDField(unique=True, editable=False,primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Member'
        ordering = ['name']
class EventRegistration(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('Pending', 'Pending'),('Completed', 'Completed'),('Failed', 'Failed'))
    
    PAYMENT__CHOICES = (
        ('Cash', 'Cash'),('Online', 'Online'),('UPI', 'UPI'))
    
    uuid = models.UUIDField(unique=True, editable=False,primary_key=True, default=uuid.uuid4)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='event_registrations')
    registration_date = models.DateField(auto_now_add=True)
    total_members = models.PositiveIntegerField(default=1)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    members = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='event_registrations', null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT__CHOICES, default='Cash')
    payment_id = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.user.email} - {self.event.name}"