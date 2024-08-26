from django.db import models


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50)
    # Create your models here.
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class ProductModel(models.Model):
    product_name = models.CharField(max_length=80)
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=0)
    descriptions = models.TextField()
    image = models.FileField(upload_to='product_image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class CartModel(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    user_product_quantity = models.IntegerField(default=0)
    user_add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user_product})"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
