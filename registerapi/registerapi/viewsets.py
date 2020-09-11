from rest_framework import viewsets
from . import models
from . import serializers

class usersViewset(viewsets.ModelViewSet):
    queryset = models.users.objects.all()
    serializer_class = serializers.usersSerializer