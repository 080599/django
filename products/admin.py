from django.contrib import admin
from .models import CategoryModel,ProductModel,CartModel
@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields =['category_name']
    list_display=['id','category_name','created_at']
    list_filter = ["created_at"]
    ordering = ['id']
@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields=['product_mname']
    list_dispaly=['id','product_name','price','count','created_at']
    list_filter=['created_at']
    ordering=['-id']
@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    pass
#admin.site.register(CategoryModel)
# Register your models here.
