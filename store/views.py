from django.http import request
from django.shortcuts import redirect, render
from . models import *
from . forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q, query
    
def Store_list(request):
    prods=Product.objects.all()
    query = request.GET.get('q','')
    if query:
        queryset=(Q(productname__icontains=query))
        results=Product.objects.filter(queryset).distinct()
    else:
        results=[]
            
    context={'prods':prods,
             'query':query,
             'results':results}
    
    return render(request,'store/prods.html',context)

@login_required
def order(request,pk):
    st=Product.objects.get(pk=pk)
    ode=Ordeform()
    context={
        'st':st,
        'ode':ode
        }
    if request.method=="POST":
        ode=Ordeform(request.POST)
        if ode.is_valid():
            instance=ode.save(commit=False)
            instance.Product_Name=st.productname
            instance.Email=request.user.email
            instance.Name=request.user.first_name
            instance.Price=st.price
            instance.save()
            return redirect('Store')
        else:
            ode=Ordeform()    
    return render(request,'Store/order.html',context) 


# Create your views here.
