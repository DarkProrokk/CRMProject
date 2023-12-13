from django.db import models

from users.models import CustomUser


class Project(models.Model):
    title = models.CharField(max_length=32)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'

class Task(models.Model):
    title = models.CharField(max_length=32)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField()
    descriptions = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, null=True, blank=True)
    is_done = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.title} - пользователя {self.user}'
