from django.contrib import admin
from .models.product import Product
from .models.customer import Customer
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ["name","price","author"]




admin.site.register(Product,AdminProduct)
admin.site.register(Customer)