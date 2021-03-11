from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom user manager.
    """
    def _create_user(self, password, **extra_fields):
        """
        Create and save a user.
        """
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(password, **extra_fields)

    def create_superuser(self, password, **extra_fields):
        """
        Override `django.contrib.auth.models.UserManager.create_superuser`.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password, **extra_fields)


class UserRole(models.Model):
    ROLE_NAME_CHOICES = [
        ('manager', "Manager"),
        ('student', "Student"),
    ]
    name = models.CharField(max_length=100, choices=ROLE_NAME_CHOICES)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    Custom user model.
    """
    roles = models.ManyToManyField(UserRole, blank=True, related_name='roles')
    notifications = models.BooleanField(default=0)
    email = models.EmailField(blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username
