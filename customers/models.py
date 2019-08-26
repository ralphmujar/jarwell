from django.db import models


class Customer(models.Model):
   
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    address = models.CharField(max_length=150)
    contact = models.CharField(max_length=75)
    date_encoded = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.first_name

class Item(models.Model):
    
    name = models.CharField(max_length=75)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    status = models.CharField(max_length=75, default='on process')
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.item.name
