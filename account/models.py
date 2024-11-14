from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, name=None, username=None, password=None, confirm_password=None):
        if not email:
            raise ValueError('User must have an email.')
        user = self.model(name=name, username= username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user 


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'user'