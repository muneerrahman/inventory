from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDeleteView,product_index

urlpatterns = [
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view()),
    path("ui/", product_index),
]

