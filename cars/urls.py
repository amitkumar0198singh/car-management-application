from django.urls import path
from cars.views import CarView


urlpatterns = [
    path('cars/get/', CarView.as_view({'get': 'get_car'}), name='list-cars'),
    path('cars/get/<int:pk>/', CarView.as_view({'get': 'get_car'}), name='details-car'),
    path('cars/create/', CarView.as_view({'post': 'create_car'}), name='create-car'),
    path('cars/update/<int:pk>/', CarView.as_view({'put': 'update_car'}), name='update-car'), 
    path('cars/delete/<int:pk>/', CarView.as_view({'delete': 'delete_car'}), name='delete-car'),
]
