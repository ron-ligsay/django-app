from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.contrib.auth.models import User
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN",'Admin','admin'
        STUDENT = 'STUDENT','Student','student'
        TEACHER = 'TEACHER','Teacher','teacher'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *arg, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        


# class CustomAccountManager(BaseUserManager):
    
#     def create_user(self, email, user_name, first_name, password, **other_fields):
#         if not email:
#             raise ValueError(gettext_lazy('You must provide an email address'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user
#         #
#     def create_superuser(self, email, user_name, first_name, password, **other_fields):
        
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must be assinged to is_staff=True.')
        
#         if other_fields.ge('is_superuser') is not True:
#             raise ValueError('Superuser must be assigned to is_superuser=True.')
        
#         return self.create_user(email, user_name, first_name, password, **other_fields)
#         #
# # Create your models here.
# class NewUser(AbstractBaseUser, PermissionsMixin):

#     email = models.EmailField(gettext_lazy('email address'), unique=True)
#     user_name = models.CharField(max_length=150,unique=True)
#     first_name = models.CharField(max_length=150,blank=True)
#     last_name = models.CharField(max_length=150,blank=True)
#     start_date = models.DateTimeField(default=timezone.now)
#     about = models.TextField(gettext_lazy('about'),max_length=500, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
    
#     objects = CustomAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_name','first_name']

#     def __str__(self):
#         return self.user_name
    
