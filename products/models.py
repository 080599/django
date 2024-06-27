from django.db import models


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50)
    # Create your models here.
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"
class ProductModel(models.Model):
    product_name=models.CharField(max_length=80)
    price=models.FloatField()
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    count=models.IntegerField(default=0)
    descriptions=models.TextField()
    image=models.FileField(upload_to='product_image')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name
    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"
class Cart(models.Model):
    product_name=models.CharField(max_length=80)
    price=models.FloatField()
    category=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    count=models.IntegerField(default=0)
    image=models.FileField(upload_to='product_image')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name
    class Meta:
        verbose_name="Cart"

class NewsCategory(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "NewsCategory"