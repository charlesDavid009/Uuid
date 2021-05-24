from django.db import models
import uuid

# Create your models here.


class Uuid(models.Model):
    uuids = models.CharField(max_length=225)
    created = models.DateTimeField(auto_now_add=True)
