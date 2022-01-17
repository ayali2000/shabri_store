from django.urls import path
from . views import *

urlpatterns = [
    path("product/order/<int:pk>/",order,name='order'),
    path("store",Store_list,name='Store'),
]