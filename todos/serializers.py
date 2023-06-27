from rest_framework import serializers

from todos.models import Todo
from users.models import User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

