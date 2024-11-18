from django.urls import path
from account.views import RegistrationView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('sign-up/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
]
