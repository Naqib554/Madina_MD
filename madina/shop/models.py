from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=30)
    publish_date=models.DateField()



