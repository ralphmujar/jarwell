from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
        path('customers/', views.CustomersList.as_view(), name='customers'),
        path('customer/create/', views.CustomerCreate.as_view(), name='customer_create'),
        path('customer/update/<int:pk>', views.CustomerUpdate.as_view(), name='customer_update'),

        path('items/', views.ItemsList.as_view(), name='items_list'),
        path('item/create/', views.ItemCreate.as_view(), name='item_create'),
        path('order/create/', views.OrderCreate.as_view(), name='order_create'),
]
