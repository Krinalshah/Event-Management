from django.urls import include, path
from .views import OrganizationViewSet
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
# router.register(r'events', EventViewSet)
router.register(r'organizations', OrganizationViewSet, basename='organizations')

urlpatterns = [
    path('', include(router.urls)),
]