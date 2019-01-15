# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models

class Order(models.Model):
    orderid = models.CharField(max_length=50)
    otp = models.IntegerField()
    status = models.IntegerField(default = 0)

    def __str__(self):
        return self.orderid
