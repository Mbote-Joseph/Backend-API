from django.db import models

# Create your models here.
class Item(models.Model):
    farmerName = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')



    def __str__(self):
        return self.name + ' - ' + str(self.price) + ' - ' + str(self.quantity)