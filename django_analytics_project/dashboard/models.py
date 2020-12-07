from django.db import models

# Create your models here.
class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)

class Download(models.Model):
    date = models.DateField()
    daily_downloads = models.IntegerField()

    def __str__(self):
        return str(self.date)