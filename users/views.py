from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import CustomUserSerializer,MyObtainTokenSerializer
from .permissions import ClientPermission,AdminPermission

class ClientListViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,ClientPermission]

    queryset=CustomUser.objects.filter(user_type="Client")
    serializer_class=CustomUserSerializer
    lookup_field='id'

class AdminListViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated,AdminPermission]

    queryset=CustomUser.objects.filter(user_type="Admin")
    serializer_class=CustomUserSerializer
    lookup_field='id'


class MyObtainTokenView(TokenObtainPairView):
    serializer_class = MyObtainTokenSerializer
    