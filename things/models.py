from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=15,unique=True,primary_key=True,blank=False)
    description = models.CharField(max_length=120,unique=False,blank=True,)
    quantity = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])

