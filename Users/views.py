from django.shortcuts import redirect, render
from . forms import *

# Create your views here.

def signUp(request):
    form=CreateUser()
    context={'form':form}
    if request.method=='POST':
        form=CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('level_100')
        else:
            form=CreateUser()
    return render(request,'Users/sign_up.html',context)
