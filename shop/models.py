# http://www.lexev.org/2015/trying-json-combo-django-and-postgresql/

from django.db import models
# from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    attributes = JSONField()

    def __str__(self):
        return self.name