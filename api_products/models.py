from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500)
    image_url = models.URLField(max_length=1000)
      

    def __str__(self):
        return self.name