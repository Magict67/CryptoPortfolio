from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=20, decimal_places=10)
    price_purchased = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.symbol})"