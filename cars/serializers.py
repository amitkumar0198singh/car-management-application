from rest_framework import serializers
from cars.models import CarImage, Car


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['image']
        
class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, required=False)
    class Meta:
        model = Car
        fields = ['title', 'description', 'tags', 'images']
        
    def validate_images(self, value):
        if len(value)>10:
            raise serializers.ValidationError('User can upload upto 10 images only.')
        return value
    
    def create(self, validated_data):
        images = validated_data.pop('images', [])
        car = Car.objects.create(**validated_data)
        images = self.context.get('request').FILES.getlist('images')
        try:
            car_images = [CarImage(car=car, image=image) for image in images]
            CarImage.objects.bulk_create(car_images)
        except Exception as e:
            raise serializers.ValidationError(f'Error saving images: {str(e)}')
        return car
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.tags = validated_data.get('tags', instance.tags)
        images = self.context.get('request').FILES.getlist('images')
        if images:
            instance.images.all().delete()
            try:
                car_images = [CarImage(car=instance, image=image) for image in images]
                CarImage.objects.bulk_create(car_images)
            except Exception as e:
                raise serializers.ValidationError(f'Error saving images: {str(e)}')
        instance.save()
        return instance