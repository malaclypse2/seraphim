from django.db import models

# Create your models here.
class CharacterIcon(models.Model):
    url = models.URLField()

class Character(models.Model):
    icon = models.ForeignKey(CharacterIcon)
    name = models.CharField(max_length=200)
    profession = models.CharField('class', max_length=50)
    level = models.IntegerField()
    base_hp = models.IntegerField()

