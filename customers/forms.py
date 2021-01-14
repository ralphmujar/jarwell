from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Customer, Item, Order, OrderItem


class  DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForm(ModelForm):

    class Meta:
        model = Customer    
        #fields = ['name', 'description', 'price']
        fields = '__all__'

class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        size_choices = [('extra small', 'extra small'),
                ('small', 'small'), 
                ('medium', 'medium'),
                ('large', 'large'),
                ('extra large', 'extra large'),
                ]
        widgets = {'size': forms.Select(choices=size_choices)}

class OrderForm(ModelForm):    
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemForm(ModelForm):

    class Meta:
        model = OrderItem
        fields = ['item', 'qty']


OrderItemFormset = inlineformset_factory(Order, OrderItem, form=OrderItemForm)
