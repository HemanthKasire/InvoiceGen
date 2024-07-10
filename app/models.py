from django.db import models
import datetime

class seller(models.Model):
    name = models.CharField(max_length=50, default="Archana Reddy P")
    address = models.CharField(max_length=150, default="ITI Township, Bengaluru")
    phone = models.CharField(max_length=15, default='+91 8171415434')
    date = models.DateTimeField(default=datetime.datetime.today)

class buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    purchase_date = models.DateTimeField(default=datetime.datetime.now)

class producat(models.Model):
    seller = models.ForeignKey(seller, on_delete=models.CASCADE, null=True, default=None)
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)
