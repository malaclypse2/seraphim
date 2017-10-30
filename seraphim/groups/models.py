from django.db import models
from statistics import mean

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=200)
    crt_dttm = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField('characters.Character')
    def __str__(self):
        return '{self.name}'.format(self=self)
    def avg_level(self):
        levels = [character.level for character in self.members.all()]
        avg = mean(levels)
        return "{:.1}".format(avg)
