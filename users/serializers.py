from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','password', 'email', 'user_type']
    def validate(self,data):
        if data['username']:
            if CustomUser.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("Username is taken")
    
        if data['email']:
            if CustomUser.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError("Email is taken")
        return data
    def create(self, validated_data):
        user=CustomUser.objects.create(username=validated_data['username'],email=validated_data['email'],user_type=validated_data['user_type'])
        user.set_password(validated_data['password'])
        user.save()
        
        return validated_data 

class MyObtainTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls,user):
        token = super(MyObtainTokenSerializer,cls).get_token(user)

        #custom claims
        token['username'] = user.username
        token['password'] = user.password
        token['user_type'] = user.user_type
        
        return token