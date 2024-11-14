from django.urls import include, path
from cars.views import CarView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cars', CarView, basename='cars')

urlpatterns = [
    path('', include(router.urls)),
]
