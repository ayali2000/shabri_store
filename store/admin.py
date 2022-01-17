from django.contrib import admin
from . models import *

class OrdeAdmin(admin.ModelAdmin):
        list_display=('Name','Email','Phone_Number','Product_Name','quantity','Price','Address','Order_Status','date')

class ProductAdmin(admin.ModelAdmin):
        list_display=['productname','descriptions','price']
    
admin.site.register(Product,ProductAdmin),
admin.site.register(Order,OrdeAdmin)   
# Register your models here.
