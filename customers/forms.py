from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer    
        #fields = ['name', 'description', 'price']
        fields = '__all__'
