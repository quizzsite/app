from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import os

# from .backends import AuthUserBackend

def photodir(instance, filename): return os.path.join('account', 'photos', instance.user.username, '%Y-%m-%d', filename)
def bannerdir(instance, filename): return os.path.join('account', 'photos', instance.user.username, '%Y-%m-%d', filename)

class Purchase(models.Model):
    price = models.IntegerField()
    courses = models.ManyToManyField('lessons.Course')

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    def get_by_natural_key(self, email):
        return self.get(email=email)
class User(AbstractUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    username = None
    email = models.EmailField(unique=True)
    confirmed = models.BooleanField(default=False)
    conf_key = models.CharField(default="", max_length=99999999)
    photo = models.ImageField(upload_to=photodir, default="account/photos/user.svg")
    banner = models.ImageField(upload_to=bannerdir, default="account/photos/user.svg")
    mailing = models.BooleanField(default=True)

    objects = UserManager()

class Student(User):
    verbose_name = 'Student'
    courses = models.ManyToManyField('lessons.Course')
    purchases = models.ManyToManyField(Purchase)

class Teacher(User):
    verbose_name = 'Teacher'
    subject = models.ForeignKey('lessons.Subject', on_delete=models.DO_NOTHING)