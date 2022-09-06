# http://www.lexev.org/2015/trying-json-combo-django-and-postgresql/

# Подходящий пример!!!!!!!!
# https://www.cybertec-postgresql.com/en/json-postgresql-how-to-use-it-right/#json-good-example
# https://ru.stackoverflow.com/questions/1222063/%D0%9A%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D1%8F%D1%82%D1%8C-%D1%85%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-json-%D0%B4%D0%BB%D1%8F-%D0%BA%D0%B0%D0%B6%D0%B4%D0%BE%D0%B9-%D0%BA%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8
# https://ru.stackoverflow.com/questions/697810/%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0-django-mptt
# https://tretyakov.net/post/drevovidnye-kategorii-v-django/
# https://github.com/abogushov/django-admin-json-editor

from django.db import models


# from django.db.models import JSONField

# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     price = models.IntegerField()
#     attributes = JSONField()

#     def __str__(self):
#         return self.name


from django_jsonform.models.fields import JSONField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()

    # Динамическая схема
    # https://django-jsonform.readthedocs.io/en/stable/guide/choices.html#dynamic-choices
    
    ITEMS_SCHEMA = {
        "type": "object",
        "title": "Характеристики",
        "keys": {
            "brand": {
                "type": "string",
                "title": "Бренд",
            },
            "number": {
                "type": "integer",
                "title": "Кол-во на складе",
                'default': 0,
            },
            'items': {
                'type': 'string',
                'choices': ['Eggs', 'Juice', 'Milk'],
                'default': 'Milk'
            },

        },
        "additionalProperties": {
            "type": "string"
        }
    }
    attributes = JSONField(schema=ITEMS_SCHEMA)

    def __str__(self):
        return self.name