from django.db import models

# Create your models here.

class Day(models.Model):
    crt_dttm = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=200, default='There we were...')
    group = models.ForeignKey('groups.Group')
    def __str__(self):
        fmt_dttm = self.crt_dttm.strftime("%B %d, %Y %I:%M%p")
        return '{self.desc}, ({self.group}) - created {fmt_dttm}'.format(self=self, fmt_dttm = fmt_dttm)

class Combat(models.Model):
    game_day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return '{self.name}, {self.profession}:{self.level} - {self.base_hp} HP'.format(self=self)

class Round(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)

    def __str__(self):
        return '{self.name}, {self.profession}:{self.level} - {self.base_hp} HP'.format(self=self)

class StatusEffectType(models.Model):
    typ = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return '{self.name}, {self.profession}:{self.level} - {self.base_hp} HP'.format(self=self)

class StatusEffect(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    effect_typ = models.ForeignKey(StatusEffectType)
    effect_val = models.IntegerField(default=0)
    effect_txt = models.CharField(max_length=50)

    def __str__(self):
        return '{self.name}, {self.profession}:{self.level} - {self.base_hp} HP'.format(self=self)

class Wound(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    amount = models.IntegerField()
    bandaged = models.BooleanField(default=False)

    def __str__(self):
        return '{self.name}, {self.profession}:{self.level} - {self.base_hp} HP'.format(self=self)

class Heal(models.Model):
    combat = models.ForeignKey(Combat, on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return '{self.name}, {self.profession}:{self.level} - {self.base_hp} HP'.format(self=self)
