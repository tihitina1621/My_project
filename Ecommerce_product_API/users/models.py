from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):   #creates a regular users
        if not email:
            raise ValueError('Please input a valid Email.')
        
        email = self.normalize_email(email)       #normalizes the email to a standard format
        user = self.model(username=username, email=email, **extra_fields)
        validate_password(password, user)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)         
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)          #the created users will have admin privilage
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    name = models.CharField(max_length=200, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email


