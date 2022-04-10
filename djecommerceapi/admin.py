from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'isbn', 'pages', 'price', 'stock', 'status')
    search_fields = ['title', 'category',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'status')
    search_fields = ['name', 'category',]