from django.db import models


class Building(models.Model):
    price = models.IntegerField()
    surface = models.IntegerField()
    room_count = models.IntegerField()
    address = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
