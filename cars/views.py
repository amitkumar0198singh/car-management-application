from rest_framework.response import Response
from rest_framework import viewsets, status
from cars.serializers import CarSerializer
from cars.services import get_all_car
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser


class CarView(viewsets.ViewSet):
    parser_classes = [MultiPartParser, FormParser]
    
    def get_car(self, request, pk=None):
        keyword = request.query_params.get('search', None)
        if pk is not None:
            serializer = CarSerializer(get_all_car(owner=request.user, pk=pk))
            return Response({'status': True, 'message': 'Car Fetched', 'car': serializer.data}, status=status.HTTP_200_OK)
        else:
            serializer = CarSerializer(get_all_car(request.user, keyword=keyword), many=True)
            return Response({'status': True, 'message': 'Cars fetched.', 'cars': serializer.data}, status=status.HTTP_200_OK)
    
    
    def create_car(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({'status': True, 'message': 'Car created.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': False, 'message': 'Validation error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def update_car(self, request, pk):
        serializer = CarSerializer(get_all_car(owner=request.user, pk=pk), data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'Car updated', 'car': serializer.data}, status=status.HTTP_200_OK)
        return Response({'status': False, 'message': 'Validation Failed', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete_car(self, request, pk):
        car = get_all_car(owner=request.user, pk=pk)
        car.delete()
        return Response({'status': True, 'meesage': 'Car deleted'}, status=status.HTTP_200_OK)