from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class CharacterIcon(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    sort_key = models.IntegerField(default=999)
    def __str__(self):
        return '[{self.sort_key:03d}] {self.name}'.format(self=self)

class Character(models.Model):
    name = models.CharField(max_length=200)
    # Meta information
    owner = models.ForeignKey(
        'users.user', on_delete=models.SET_NULL, null=True)
    public = models.BooleanField(default=True)
    # Basic Character stats
    icon = models.ForeignKey(CharacterIcon, on_delete=models.SET_NULL, null=True)
    profession = models.CharField('class', max_length=50)
    level = models.IntegerField()
    base_hp = models.IntegerField()
    av_short = models.CharField('AV (Short)', max_length=50, default='AV: ')
    av_long = models.TextField('AV (Long), and other notes.', blank=True)
    campaign_status = models.TextField(blank=True)
    def __str__(self):
        return '{self.name}, {self.profession}:{self.level} - {self.base_hp} HP'.format(self=self)
    def get_absolute_url(self):
        return reverse('character_edit', kwargs={'pk': self.pk})
        
