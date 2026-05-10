from .models import Organization, Event, Members, EventRegistration
from user.models import CustomUser
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=False, allow_blank=True)
    user = serializers.SlugRelatedField(slug_field='email', queryset=CustomUser.objects.all(), required=True)
    # user = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Organization
        fields = ['name', 'address', 'user']
        read_only_fields = ['uuid']


class EventSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=True)
    time = serializers.TimeField(required=True)
    location = serializers.CharField(required=True,max_length=1000)
    organization = serializers.SlugRelatedField(slug_field='name', queryset=Organization.objects.none(), required=True)
    class Meta:
        model = Event
        fields = ['name', 'date','time', 'location', 'description',"organization", "capacity", "image"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            self.fields['organization'].queryset = Organization.objects.filter(user=request.user)
    
class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['name', 'email', 'phone_number', 'event']

class EventRegistrationSerializer(serializers.ModelSerializer):
    PAYMENT_CHOICES = (
        ('Cash', 'Cash'),('Online', 'Online'),('UPI', 'UPI'))
    members = MembersSerializer(many=True)
    event = serializers.SlugRelatedField(slug_field='name', queryset=Event.objects.all(), required=True)
    user = serializers.SlugRelatedField(slug_field='email', queryset=CustomUser.objects.none(), required=True)
    registration_date = serializers.DateField(read_only=True)
    payment_method = serializers.ChoiceField(choices=PAYMENT_CHOICES, required=True)
    class Meta:
        model = EventRegistration
        fields = ['event', 'user', 'registration_date', 'total_members', 'payment_status', 'members', 'payment_method']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            self.fields['user'].queryset = CustomUser.objects.filter(email=request.user.email)