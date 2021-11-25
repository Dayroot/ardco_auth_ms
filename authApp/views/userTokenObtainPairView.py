#DJANGO REST FRAMEWORK
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import exceptions

#CUSTOM SERIALIZER
from authApp.serializers import UserTokenObtainPairSerializer
        
class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer