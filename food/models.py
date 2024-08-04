from django.db import models


# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    # item_image = models.CharField(max_length=500, default="https://images.unsplash.com/photo-1572373549709-c78b9d41b864")
    item_image = models.ImageField(upload_to="food_images")

    def __str__(self):
        return self.item_name

   
