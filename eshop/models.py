from django.db.models import *


# Create your models here.

class product(Model):
    title = CharField(max_length=30)
    description = TextField()
    cost = FloatField()
    in_stock = IntegerField()

class personal_info(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    address = TextField()
    number = IntegerField()

class order(Model):
    product = ForeignKey(product, on_delete=CASCADE, default=None)
    quantity = IntegerField()
    personal_info = ForeignKey(personal_info, on_delete=CASCADE, default=None)



