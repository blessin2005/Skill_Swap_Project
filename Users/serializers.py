from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    bio = serializers.CharField(
        source='profile.bio',
        required=False,
        allow_blank=True
    )

    created_at = serializers.DateTimeField(
        source='profile.created_at',
        read_only=True
    )

    class Meta:
        model = User

        fields = [
            'id',
            'username',
            'email',
            'password',
            'bio',
            'created_at'
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):

        profile_data = validated_data.pop(
            'profile',
            {}
        )

        password = validated_data.pop(
            'password'
        )

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        UserProfile.objects.create(
            user=user,
            **profile_data
        )

        return user