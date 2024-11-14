from cars.models import Car
from account.models import User 
from django.db.models import QuerySet

def get_all_car(owner: User) -> QuerySet:
    return Car.objects.filter(owner=owner)