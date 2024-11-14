from rest_framework.response import Response
from rest_framework import viewsets, status
from cars.serializers import CarSerializer
from cars.services import get_all_car
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser


class CarView(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    @action(detail=False, methods=['get'], url_path='get-car', url_name='get-car')
    def get_car(self, request):
        serializer = self.get_serializer(get_all_car(request.user), many=True)
        return Response({'status': True, 'message': 'Cars fetched.', 'cars': serializer.data}, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['post'], url_path='create', url_name='create-car')
    def create_car(self, request):
        import pdb; pdb.set_trace()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({'status': True, 'message': 'Car created.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
