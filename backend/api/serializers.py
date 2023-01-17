from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['categories', 'email']


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.New
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
