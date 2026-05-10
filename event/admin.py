from django.contrib import admin

from .models import Organization, Event, Members, EventRegistration
admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(EventRegistration)

# Register your models here.
