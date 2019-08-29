from django import forms
from .models import Customer, Item, Order

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer    
        #fields = ['name', 'description', 'price']
        fields = '__all__'

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        size_choices = [('small', 'small'), 
                ('medium', 'medium'),
                ('large', 'large')]
        widgets = {'size': forms.Select(choices=size_choices)}

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = '__all__'
