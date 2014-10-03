from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=128)


class Player(models.Model):
    name = models.CharField(max_length=128)
    team = models.ForeignKey(Team)











