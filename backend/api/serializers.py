from rest_framework import serializers
from . import models


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.New
        fields = '__all__'
