from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class UserView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    @extend_schema(operation_id="user_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
