from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from socialnetworkapp.views import SubscriptionViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]