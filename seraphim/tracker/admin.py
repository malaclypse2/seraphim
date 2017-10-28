from django.contrib import admin

# Register your models here.
from .models import Day, Combat, Round, StatusEffectType, StatusEffect, Heal, Wound
admin.site.register(
    [Day, Combat, Round, StatusEffectType, StatusEffect, Heal, Wound])
