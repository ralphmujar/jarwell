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

    payment_choices = [ ('0', 'Not yet paid'),
            ('1', 'Partially paid'),
            ('2', 'Fully paid')]
    
    payment_status = forms.ChoiceField(choices = payment_choices)
    
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
                'item' : forms.Select(attrs={'id' : 'item' }),
                'qty' : forms.TextInput(attrs={'id' : 'qty' }),
                'shipping_fee' : forms.TextInput(attrs={'id' : 'shipping_fee' }),
                'total_price' : forms.TextInput(attrs={'id' : 'total_price' }),
                }

