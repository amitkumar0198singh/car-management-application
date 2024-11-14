from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from account.models import User


class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
        except User.DoesNotExist:
            return None
        if user.check_password(password) and self.user_can_authenticate(user=user):
            return user
        return None