from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'username', 'email', 'first_name', 'last_name']
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_instance = self.Meta.model(**validated_data)
        if password is not None:
            # If a password is provided, it sets the password on the user instance using the set_password() method,
            # which hashes the password for security.
            user_instance.set_password(password)
        user_instance.save()
        return user_instance
