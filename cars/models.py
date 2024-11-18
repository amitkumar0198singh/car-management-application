from django.db import models
from account.models import User


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, db_column='owner', related_name='cars')
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    tags = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cars'
    
class CarImage(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE, db_column='car', related_name='images')
    image = models.ImageField(upload_to='images/')
    
    class Meta:
        db_table = 'car_images'