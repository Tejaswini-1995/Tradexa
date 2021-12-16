from os import getenv
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email_id, **extra_fields):
        user = None
        email = self.normalize_email(email_id)
        user = self.model(email=email, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, email, **extra_fields):
        user = self._create_user(email, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = None
        user = self.model(
            email=email,


            password=password,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUserModel(AbstractBaseUser):
    class Meta:
        verbose_name = "User"

    def __str__(self):
        return f"{self.first_name} | {self.email}"

    user_id = models.AutoField(primary_key=True, editable=False, unique=True)
    email = models.CharField(max_length=255, unique=True, null=True)
    username = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    password = models.CharField(max_length=255, null=True)

    # Profile Related Attributes.


    first_name = models.CharField(max_length=50, db_column="first name", null=True)
    last_name = models.CharField(max_length=50, db_column="last name", null=True)
    # change it if required mobile

    mobile = models.CharField(max_length=15, null=True, unique=True)


    REQUIRED_FIELDS = ["first_name"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()

