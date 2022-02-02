from ast import mod
from django.contrib import admin

# Register your models here.
from .models import Product, Picture, Category, Faq

class PicturesInline(admin.StackedInline):
    model = Picture
    fields = ( 'picture','image_name','image_tag', )
    readonly_fields = ('image_tag',)
    extra=0

class FAQsInline(admin.StackedInline):
    model = Faq
    fields = ( 'question','answer')
    extra=0

class ProductInline(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'original_price', 'discounted_price')
    inlines = [PicturesInline, FAQsInline]

admin.site.register(Product,ProductInline )
admin.site.register(Category)