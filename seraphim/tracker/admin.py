from django.contrib import admin

# Register your models here.
from .models import Day, Combat, StatusEffectType, StatusEffect, Heal, Wound
admin.site.register(
    [Day, Combat, StatusEffectType, StatusEffect, Heal, Wound])
