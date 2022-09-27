from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=210)


class Category(models.Model):
    img = models.ImageField(upload_to='category/')
    name = models.CharField(max_length=210)


class Food(models.Model):
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)
    name = models.CharField(max_length=12121)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=23232323)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    seats = models.IntegerField()
    time = models.TimeField(auto_now_add=True)
    quantity = models.IntegerField()
    special_request = models.CharField(max_length=1212121, null=True, blank=True)


class Table(models.Model):
    status = (
        (1, 'Empty'),
        (2, 'Busy')
    )
    busyness = models.IntegerField(choices=status, default=1)
    number = models.IntegerField()

