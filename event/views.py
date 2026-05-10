from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Organization
from .serializers import OrganizationSerializer
from rest_framework.permissions import DjangoModelPermissions
# Create your views here.
class OrganizationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        return Organization.objects.filter(user=self.request.user)

