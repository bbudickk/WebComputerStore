from django.urls import reverse

from django.db import models
from django.conf import settings

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    photo = models.ImageField(upload_to="photos", default='photos/1.jpg')
    description = models.TextField()
    release_date = models.DateField()
    delivery_date = models.DateField()
    on_storage = models.BooleanField()

    def get_product(self):
        return reverse('product', kwargs={'product_id': self.pk})

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Корзина для {self.user.username} | {self.product.name}'

    def sum(self):
        return self.count * self.product.price


