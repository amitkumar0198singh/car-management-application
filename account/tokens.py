from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens(user):
    return RefreshToken.for_user(user)
    