from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PG

class UserRegistrationSerializer(serializers.ModelSerializer):
    pg_name = serializers.CharField()
    pg_address = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'pg_name', 'pg_address']

    def create(self, validated_data):
        pg_name = validated_data.pop('pg_name')
        pg_address = validated_data.pop('pg_address')

        # Create user
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email')
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create PG
        PG.objects.create(
            owner=user,
            pg_name=pg_name,
            pg_address=pg_address
        )

        return user


