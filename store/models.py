from django.db import models

class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    productname=models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    descriptions=models.TextField()
    p_image=models.ImageField(blank=True, null=True,upload_to='products')


class Order(models.Model):
    ORDER_STATUS=(
        ("Pending","Pending"),
        ("Received","Received"),
    )
    Order_Status=models.CharField(max_length=50,choices=ORDER_STATUS,default='Pending')
    Name=models.CharField(max_length=155)
    Phone_Number=models.CharField(max_length=15)
    Email=models.EmailField()
    Product_Name=models.CharField(max_length=255)
    quantity=models.PositiveIntegerField(default=1)
    Price=models.CharField(max_length=199)
    Address=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-date']

# Create your models here.
