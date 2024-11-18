from rest_framework_simplejwt.authentication import JWTAuthentication as JWTAuth
from rest_framework.exceptions import AuthenticationFailed


class JWTAuthentication(JWTAuth):
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except AuthenticationFailed as error:
            raise AuthenticationFailed(f'{error}')
        
    def get_user(self, validated_token):
        try:
            user = super().get_user(validated_token)
        except Exception:
            raise AuthenticationFailed('Authentication failed.')
        return user