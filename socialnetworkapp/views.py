from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Subscription, User
from .serializers import SubscriptionSerializer, UserSerializer
import datetime

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        subscriber = request.data.get('subscriber')
        subscribed_to = request.data.get('subscribed_to')
        
        if subscriber == subscribed_to:
            return Response({'error': 'Нельзя подписаться на самого себя.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Subscription.objects.filter(subscriber=subscriber, subscribed_to=subscribed_to).exists():
            return Response({'error': 'Вы уже подписаны на этого пользователя.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        instanse = self.get_object()
        serializer = self.get_serializer(instanse)
        data = serializer.data
        
        subscriber_username = instanse.subscriber.username
        subscribed_to_username = instanse.subscribed_to.username
        
        data['subscriber'] = subscriber_username
        data['subscribed_to'] = subscribed_to_username
        
        return Response(data)
