from django.db import models
from stationery.choices import order_choice

class Material(models.Model):
     # order provided
    title                   = models.CharField(max_length = 100)
    material_type           = models.CharField(max_length = 60, choices = order_choice)
    description             = models.TextField()
    # stationery_name        = models.ForeignKey(stationery = '')

