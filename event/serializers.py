from .models import Organization
from rest_framework import serializers
from user.models import CustomUser


class OrganizationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=False, allow_blank=True)
    user = serializers.SlugRelatedField(slug_field='email', queryset=CustomUser.objects.all(), required=True)
    # user = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Organization
        fields = ['name', 'address', 'user']