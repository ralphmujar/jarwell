from django.db import models
import computed_property



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
    shipping_fee = models.DecimalField(max_digits=7, decimal_places=2)
    payment_status = models.IntegerField(default=0)
    shipping_status = models.BooleanField(default=False)
    notes = models.TextField(default="None")
    date = models.DateField(auto_now_add=True)

    @property
    def total_order(self):
        order_items = OrderItem.objects.filter(order_id=self.id)
        sum = 0
        for order_item in order_items:
            sum = sum + order_item.price
        return ( sum + float(self.shipping_fee) )


    @property
    def total_qty(self):
        order_items = OrderItem.objects.filter(order_id=self.id)
        total_qty = 0
        for order_item in order_items:
            total_qty = (order_item.qty + total_qty)
        return total_qty


    def __str__(self):
        return self.customer.first_name.title() +" "+self.customer.last_name.title()

class OrderItem(models.Model):

    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    #bulk_price = computed_property.ComputedDecimalField(max_digits=7, decimal_places=2, compute_from='price')

    @property
    def price(self):
         return self.qty * self.item.price


    def __str__(self):
        return self.item.name +" "+ str(self.qty)
