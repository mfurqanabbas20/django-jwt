from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # kya kya cheezein return krni hain user serializer call pe
    # aik tarah se response class hai
    class Meta:
        model = User 
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    # kya kya cheezein return krni hain user serializer call pe
    # aik tarah se response class hai
    class Meta:
        model = User 
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        return user
    
    # use model serializer when we want to create data
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)