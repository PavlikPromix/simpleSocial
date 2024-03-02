from rest_framework import serializers
from .models import Subscription, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'subscriptions_count', 'subscribers_count']
        
    def get_subscriptions_count(self, obj):
        return obj.subscriptions_count()

    def get_subscribers_count(self, obj):
        return obj.subscribers_count()
        
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['subscriber', 'subscribed_to']
