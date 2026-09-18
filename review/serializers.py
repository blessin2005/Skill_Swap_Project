from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    reviewer_username = serializers.CharField(
        source='reviewer.username',
        read_only=True
    )

    reviewed_username = serializers.CharField(
        source='reviewed_user.username',
        read_only=True
    )

    class Meta:
        model = Review

        fields = [
            'id',
            'reviewer',
            'reviewer_username',
            'reviewed_user',
            'reviewed_username',
            'rating',
            'comment',
            'created_at'
        ]

        read_only_fields = [
            'id',
            'reviewer',
            'created_at'
        ]

    def validate_rating(self, value):

        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 1 and 5."
            )

        return value

    def validate(self, data):

        request = self.context.get('request')

        if request and request.user.is_authenticated:

            if data.get('reviewed_user') == request.user:
                raise serializers.ValidationError(
                    "You cannot review yourself."
                )

        return data