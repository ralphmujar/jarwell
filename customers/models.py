from django.db import models


class Customer(models.Model):
   
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    address = models.CharField(max_length=150)
    contact = models.CharField(max_length=75)
    date_encoded = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.first_name

