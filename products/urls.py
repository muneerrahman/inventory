from django.urls import path
from .views import product_list_create,product_retrieve_update_delete,product_index

urlpatterns = [
    path('products/', product_list_create),
    path('products/<int:pk>/', product_retrieve_update_delete),
    path("ui/", product_index),
]

