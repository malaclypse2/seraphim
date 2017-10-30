from django.contrib import admin

# Register your models here.
from .models import Combat, StatusEffectType, StatusEffect, Heal, Wound
admin.site.register(
    [Combat, StatusEffectType, StatusEffect, Heal, Wound])
