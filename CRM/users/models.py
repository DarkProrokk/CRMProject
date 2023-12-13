from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    first_name = None
    last_name = None

    class Meta:
        permissions = (('tier_1', "Пользователь может видеть свои задачи и проекты, в которых есть его задачи."),
                       ('tier_2', "Пользователь может видеть все задачи и все проекты. Может создавать проекты и задачи"
                                  "в своих проектах."),
                       ('tier_3(Admin)', "Может видеть все проекты и задачи. Может создавать проекты и задачи во всех"
                                         " проектах"))
