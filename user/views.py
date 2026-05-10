from xmlrpc import client

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import CustomUserSerializer, MobileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class SignInView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            return Response({'message': 'You are already logged in'}, status=status.HTTP_200_OK)
        
        created_user = CustomUserSerializer(data=request.data)
        if created_user.is_valid():
            created_user.save()
            return Response({**created_user.data, 'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(created_user.errors, status=status.HTTP_400_BAD_REQUEST)


# class EventViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

class ProfileView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)


# def send_sms(request):
#     from twilio.rest import Client
#     from django.conf import settings
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     verification = client.verify \
#     .v2 \
#     .services('VAf609f543e2dbf82743256ef4f9878c03') \
#     .verifications \
#     .create(to='+9898384427', channel='sms')

#     return Response({"sid": verification.sid})
