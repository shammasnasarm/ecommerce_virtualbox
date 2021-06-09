from django.db import models

# Create your models here.

class Product(models.Model):
    SKU_No = models.CharField(max_length=50)
    Product_Name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='product', null=True, blank=True)

    def __str__(self):
        return self.SKU_No
