from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Customer(User):
    class Meta:
        proxy = True

    @property
    def get_products(self):
        return []


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
