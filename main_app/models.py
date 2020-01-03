from django.db import models
from django.urls import reverse

class list_item(models.Model):
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

