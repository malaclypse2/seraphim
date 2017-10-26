from django.db import models

# Create your models here.
class CharacterIcon(models.Model):
    url = models.URLField()

class Character(models.Model):
    icon = models.ForeignKey(CharacterIcon)
    name = models.CharField()
    profession = models.CharField('class')
    level = models.IntegerField()
    base_hp = models.IntegerField()

