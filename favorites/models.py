from django.db import models

from core.models import Product
from users.models import User


class Favorite(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, verbose_name="Пользователь")

    def __str__(self):
        return self.user.username


class FavoriteProduct(Favorite):
    class Meta:
        db_table = "FavoriteProduct"

    product = models.ForeignKey(Product, verbose_name="Продукт")
