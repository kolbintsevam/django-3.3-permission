from django.contrib.auth.models import User
from django.forms import ValidationError
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        usr = self.context["request"].user
        count = Advertisement.objects.filter(creator=usr, status='OPEN').count()
        if 'status' in data:
            if data['status'] == 'CLOSED':
                return data
            elif data['status'] == 'OPEN':
                if count >= 10:
                    raise ValidationError('Превышено колличество открытыз объявлений')
                return data
        else:
            if count >= 10:
                raise ValidationError('Превышено колличество открытыз объявлений')
            return data

