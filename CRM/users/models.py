from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    first_name = None
    last_name = None

    class Meta:
        permissions = (('tier_1', "Can view own tasks and tasks project"),
                       ('tier_2', "Can view all tasks and projects, can create projects and tasks in own projects"),
                       ('tier_3(Admin)', "Can view, create and edit all tasks and projects"))