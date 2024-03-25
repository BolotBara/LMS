from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Client(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"


class Purchase(models.Model):
    client = models.ForeignKey(Client, related_name='purchases', on_delete=models.CASCADE)
    item = models.ManyToManyField(Item, related_name='purchases')
    def __str__(self):
        return f"{self.client}"
