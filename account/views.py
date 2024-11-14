from rest_framework.response import Response
from rest_framework import views, status
from account.serializers import RegistrationSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from account.tokens import get_tokens
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login



class RegistrationView(views.APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens(user)
            return Response(
                {
                    'status': True, 
                    'message': 'User registered successfully.', 
                    'name': serializer.data.get('name'),
                    'username': serializer.data.get('username'),
                    'email': serializer.data.get('email'),
                    'access_token': str(token.access_token),
                    'refresh_token': str(token)
                },
                status=status.HTTP_201_CREATED
            )
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username_or_email = serializer.validated_data.get('username_or_email')
            password = serializer.validated_data.get('password')
            
            user = authenticate(request=request, username=username_or_email, password=password)
            if user is not None:
                update_last_login(None, user=user)
                token = get_tokens(user=user)
                return Response(
                    {
                        'status': True,
                        'message': 'User logged in successfully.',
                        'name': user.name if user.name else None,
                        'username': user.username if user.username else None,
                        'email': user.email,
                        'access_token': str(token.access_token),
                        'refresh_token': str(token)
                    },
                    status=status.HTTP_200_OK
                )
            return Response({'status': False, 'message': 'Invalid credential.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


