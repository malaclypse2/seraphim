from django.db import models

# Create your models here.

class Combat(models.Model):
    group = models.ForeignKey('groups.Group')
    name = models.CharField(max_length=200)
    in_progress = models.BooleanField(default=True)
    crt_dttm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{self.name} - {self.group}'.format(self=self)

class StatusEffectType(models.Model):
    typ = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)
    crt_dttm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{self.typ}, {self.desc}'.format(self=self)

class StatusEffect(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    effect_typ = models.ForeignKey(StatusEffectType)
    effect_val = models.IntegerField(default=0)
    effect_txt = models.CharField(max_length=50)
    crt_dttm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{self.effect_typ.typ}, {self.effect_val}: {self.effect_typ.desc} {self.effect_txt}'.format(self=self)

class Wound(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    amount = models.IntegerField()
    bandaged = models.BooleanField(default=False)
    crt_dttm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{self.character.name}: {self.amount} HP'.format(self=self)

class Heal(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    amount = models.IntegerField()
    crt_dttm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{self.character.name}: {self.amount} HP'.format(self=self)

