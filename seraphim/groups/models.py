from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=200)
    crt_dttm = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField('characters.Character')
