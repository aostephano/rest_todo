from django.db import models

from users.models import User

app_name = 'todos'


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title + " - " + self.description

