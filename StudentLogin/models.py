from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Tickets(models.Model):
    courierid = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.courierid
        
