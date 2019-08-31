from django.db import models


class Customer(models.Model):
   
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    address = models.CharField(max_length=150)
    contact = models.CharField(max_length=75)
    date_encoded = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.first_name.title() +" "+ self.last_name.title()

class Item(models.Model):
    
    name = models.CharField(max_length=75)
    size = models.CharField(max_length=20, default='small')
    price = models.FloatField(default=0)
    date_encoded = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name.title() +" "+ self.size.upper() +" (price : "+str(self.price)+")"

class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    shipping_fee = models.DecimalField(max_digits=7, decimal_places=2)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

    payment_status = models.IntegerField(default=0)
    shipping_status = models.BooleanField(default=False)

    notes = models.TextField(default="None")
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.item.name
#
#    def compute_total_price(self):
#        self.total_price = (self.item.price * self.qty)
#        return self.total_price
#
#    def save(self, *args, **kwargs):
#        self.total_price = self.compute_total_price()
#        super(Order, self).save(*args, **kwargs)
