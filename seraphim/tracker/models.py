from django.db import models

# Create your models here.

class Day(models.Model):
    crt_dttm = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=200, default='There we were...')
    group = models.ForeignKey('groups.Group')

class Combat(models.Model):
    game_day = models.ForeignKey(Day, on_delete=models.CASCADE)

class Round(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)

class StatusEffectType(models.Model):
    typ = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)

class StatusEffect(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    effect_typ = models.ForeignKey(StatusEffectType)
    effect_val = models.IntegerField(default=0)
    effect_txt = models.CharField(max_length=50)

class Wound(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    amount = models.IntegerField()
    bandaged = models.BooleanField(default=False)

class Heal(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    amount = models.IntegerField()
