from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# category
# Customer table
# order table 
# order item
# product table

class Customer(User):
    bio = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images')

    def __str__(self):
        return self.name
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"This is Order Item {(self.product.name)}"



class Order(models.Model):
    orderItem = models.ForeignKey(OrderItem, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid')]),
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    place_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status




