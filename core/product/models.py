from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=150, null=True)
    product_description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at')
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.product_name}'


Attribute_Tbl [
   ID
   Att_Name
]

Product_Attribute_Tbl [
    Product_ID
    Attribute_ID
    Value
]