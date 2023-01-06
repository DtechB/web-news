from rest_framework import viewsets
from . import models, serializers


class NewViewSet(viewsets.ModelViewSet):
    queryset = models.New.objects.all()
    serializer_class = serializers.NewSerializer
