from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
        path('', views.CustomersList.as_view(), name='customers'),
        path('create/', views.CustomerCreate.as_view(), name='customer_create'),
        path('update/<int:pk>', views.CustomerUpdate.as_view(), name='customer_update'),
]
