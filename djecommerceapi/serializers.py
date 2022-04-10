from rest_framework import serializers
from .models import Book, Category, Product


# Book Serializer
class CategorySerialzer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


# Book Serializer
class BookSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


# Product Serializer
class ProductSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
