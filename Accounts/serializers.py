from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from Accounts.models import User


class RegisterSerializer(ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "پسورد با تکرارش برابر نیست !"})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


