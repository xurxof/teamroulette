from rest_framework.viewsets import ModelViewSet
from . import models
from . import permisssions

class TeamViewSet(ModelViewSet):
    model = models.Team
    permission_classes = (permisssions.IsOwnerPermission, )

class PlayerViewSet(ModelViewSet):
    model = models.Player
