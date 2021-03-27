from django.db.models import *


# Create your models here.

class product(Model):
    title = CharField(max_length=30)
    description = TextField()
    cost = FloatField()
    in_stock = IntegerField()
