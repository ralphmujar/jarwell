from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.messages.views import SuccessMessageMixin

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

from .models import Customer, Item, Order

@login_required(login_url='/accounts/login')
def dashboard(request):

    customer_count = Customer.objects.all().count()
    item_count = Item.objects.all().count()
    order_count = Order.objects.all().count()

    new_customers = Customer.objects.order_by('-date_encoded')[:5]

    context = {'customer_count' : customer_count,
            'item_count' : item_count,
            'order_count' : order_count,
            'new_customers' : new_customers,
            }

    return render(request, 'customers/index.html', context )


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
class CustomerUpdate(SuccessMessageMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_update.html'
    success_url = reverse_lazy('customers:customers')
    #success_url = HttpResponseRedirect(self.request.path_info)
    success_message = 'Customer successfully saved!'


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
class ItemUpdate(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'customers/item_create.html'
    success_url = reverse_lazy('customers:items_list')


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = 'customers/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.order_by('-date')





@method_decorator(login_required, name='dispatch')
class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'customers/order_create.html'
    success_url = reverse_lazy('customers:orders')


class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'customers/order_create.html'
    success_url = reverse_lazy('customers:orders')





@login_required(login_url='/accounts/login')
def get_item_price(request):

        item_id = request.GET['item_id']
        qty = request.GET['qty']
        shipping_fee = request.GET['shipping_fee']

        item = Item.objects.get(pk=item_id)

        total_price = ( (item.price * float(qty) ) + float(shipping_fee) )
        return JsonResponse(total_price, safe=False)

