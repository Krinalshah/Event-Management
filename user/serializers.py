from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import Group

class CustomUserSerializer(serializers.Serializer):
    ROLE_CHOICES = (
        ("Attendee", "Attendee"),
        ("Event Organizer", "Event Organizer"),
        ("Staff Members", "Staff Members"),
    )

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    mobile = serializers.CharField(required=True, max_length=10)
    role = serializers.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'mobile', 'first_name', 'last_name', 'role']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            mobile=validated_data.get('mobile'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=f"{validated_data.get('first_name', '')}_{validated_data.get('last_name', '')}" or validated_data['email'],
        )
        user.set_password(validated_data['password'])
        group = Group.objects.get(name=validated_data['role'])
        user.groups.add(group)
        user.save()
        return user


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['mobile']
    
    def create(self, validated_data):
        email = f"{validated_data.get('mobile')}@example.com" 
        CustomUser.objects.create(email=email,  mobile=validated_data.get('mobile'))

# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields = ['name', 'date', 'location', 'description']
  