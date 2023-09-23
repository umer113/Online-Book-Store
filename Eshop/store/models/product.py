from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    genre = models.CharField(max_length=200,default='')
    author = models.CharField(max_length=50,default='')
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()