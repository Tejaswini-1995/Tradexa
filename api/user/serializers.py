from rest_framework import serializers
from .models import CustomUserModel
from rest_framework.serializers import ValidationError
from django.contrib.auth.password_validation import validate_password




class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return CustomUserModel.objects.create(**validated_data)

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        return attrs


    class Meta:
        model = CustomUserModel
        fields = (
            "first_name",
            "last_name",
            "user_id",
            "email",
            "username",
            "otp",
            "password",

        )
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = (
            "first_name",
            "last_name",
            "user_id",

            "email",
            "username",
            "otp",
            "password",

        )
        depth = 1
