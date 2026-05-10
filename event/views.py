from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Organization, Event, Members, EventRegistration
from .serializers import OrganizationSerializer, EventSerializer
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.
class OrganizationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        return Organization.objects.filter(user=self.request.user)


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), DjangoModelPermissions()]
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

