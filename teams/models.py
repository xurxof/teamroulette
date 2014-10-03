from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=128)
    team = models.ForeignKey(Team)

    def __str__(self):
        tpl = '{} ({})'
        args = self.name, self.team
        return tpl.format(*args)











