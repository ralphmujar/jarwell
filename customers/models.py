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
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.customer.first_name.title() +" "+self.customer.last_name.title()

class OrderItem(models.Model):

    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.item.name +" "+ str(self.qty)


class OrderSummary(models.Model):

    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    shipping_fee = models.DecimalField(max_digits=7, decimal_places=2)
    total_qty = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

    payment_status = models.IntegerField(default=0)
    shipping_status = models.BooleanField(default=False)
    notes = models.TextField(default="None")

    def __str__(self):
        return self.order_id.customer.first_name +" "+ str(self.total_qty) +" doz"
