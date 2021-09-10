from django.contrib import admin
from django.urls import path
from .views import ProductList, QRAdd, QRDetail


urlpatterns = [
    path("products/", ProductList.as_view()),
    path("add-product/", QRAdd.as_view()),
    path("products/<str:pk>/", QRDetail.as_view()),
]
