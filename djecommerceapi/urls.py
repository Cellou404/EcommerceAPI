from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='singlecategory'),

    path('books/', BookList.as_view(), name='books'),
    path('books/<int:pk>/', BookDetail.as_view(), name='singlebook'),

    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='singleproduct'),
]