from rest_framework import serializers
from account.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}, 
            'confirm_password': {'write_only': True}
        }
        
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Password do not match')
        return data
    
    def create(self, validated_data):
        username = validated_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already exists.')
        email = validated_data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already registered.')
        return User.objects.create_user(**validated_data)
    
    
class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    
    def validate(self, data):
        username_or_email = data.get('username_or_email')
        if not username_or_email:
            raise ValueError('Either username or email required.')
        password = data.get('password')
        if not password:
            raise ValueError('Password is required')
        return data