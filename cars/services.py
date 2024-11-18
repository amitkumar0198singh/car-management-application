from cars.models import Car
from django.db.models import Q
from rest_framework.exceptions import NotFound


def get_all_car(owner, pk=None, keyword=None):
    query = Car.objects.filter(owner=owner)
    if pk is not None:
        try:
            return query.get(pk=pk)
        except Car.DoesNotExist:
            raise NotFound(detail='Car not found or access denied.')
    if keyword:
        query = query.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(tags__icontains=keyword))
    return query