from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def getdata(request):
    return Response({"message": "Hello World"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
