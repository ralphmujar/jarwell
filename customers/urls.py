from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [

        path('dashboard/', views.dashboard, name='dashboard'),
        path('customers/', views.CustomersList.as_view(), name='customers'),
        path('customer/create/', views.CustomerCreate.as_view(), name='customer_create'),
        path('customer/update/<int:pk>', views.CustomerUpdate.as_view(), name='customer_update'),

        path('items/', views.ItemsList.as_view(), name='items_list'),
        path('items/<int:pk>', views.ItemsDetail.as_view(), name='items_details'),
        path('item/create/', views.ItemCreate.as_view(), name='item_create'),
        path('item/update/<int:pk>', views.ItemUpdate.as_view(), name='item_update'),


        path('item/price/', views.get_item_price, name='items_price'),


        path('orders/', views.OrderList.as_view(), name='orders'),
        path('orders/<int:pk>', views.OrderDetail.as_view(), name='order_details'),

        path('order/create/', views.OrderCreate.as_view(), name='order_create'),
        path('order/update/<int:order_id>', views.order_update, name='order_update'),
        path('order/delete/<int:pk>', views.OrderDelete.as_view(), name='order_delete'),

]
