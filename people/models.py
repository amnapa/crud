from django.db import models
from django.db.models.functions import Now

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=100)
    updated_at = models.DateField(auto_now=True, db_default=Now())