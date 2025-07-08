from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)

    def get_roles(self):
        return [group.name for group in self.groups.all()]