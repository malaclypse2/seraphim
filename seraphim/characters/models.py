from django.db import models

# Create your models here.
class CharacterIcon(models.Model):
    url = models.URLField()
    def __str__(self):
        return self.url.rsplit('/', 1)[1]

class Character(models.Model):
    icon = models.ForeignKey(CharacterIcon)
    name = models.CharField(max_length=200)
    profession = models.CharField('class', max_length=50)
    level = models.IntegerField()
    base_hp = models.IntegerField()
    def __str__(self):
        return '{self.name}, {self.profession}:{self.level} - {self.base_hp} HP'.format(self=self)