from .views import SignInView
from django.urls import include, path
from .views import ProfileView
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
# router.register(r'events', EventViewSet)
router.register(r'profile', ProfileView, basename='profile')

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    # path('send-sms/', send_sms, name='send-sms'),
    path('', include(router.urls)),
]