from django.contrib import admin

# Register your models here.
from .models import Character
admin.site.register(Character)

from .models import CharacterIcon
admin.site.register(CharacterIcon)
