from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy

#views
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


#models
from .models import Customer, Item, Order

#forms
from .forms import CustomerForm, ItemForm, OrderForm

#decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class CustomersList(ListView):
    template_name = 'customers/customers.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return Customer.objects.order_by('-date_encoded')

@method_decorator(login_required, name='dispatch')
class CustomerCreate(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_create.html'
    success_url = reverse_lazy('customers:customers')

@method_decorator(login_required, name='dispatch')
class CustomerUpdate(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_update.html'
    success_url = reverse_lazy('customers:customers')


@method_decorator(login_required, name='dispatch')
class ItemsList(ListView):
    template_name = 'customers/items.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.order_by('-date_encoded')


@method_decorator(login_required, name='dispatch')
class ItemCreate(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'customers/item_create.html'
    success_url = reverse_lazy('customers:items_list')

@method_decorator(login_required, name='dispatch')
class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'customers/order_create.html'
    #gsuccess_url = reverse_lazy('customers:items_list')

