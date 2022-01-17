from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q, query
from geomatic.forms import UploadfilesForm

from geomatic.models import *

# Create your views here.
@login_required
def level_100(request):
    l_100=LearniMaterials.objects.all()
    query=request.GET.get('q','')
    if query:
        queryset=(Q(Document_name__icontains=query))|(Q(Document__icontains=query))|(Q(Year__icontains=query))|(Q(Semester__icontains=query))
        results=LearniMaterials.objects.filter(queryset).distinct()
    else:
        results=[]    
    context={'l_100':l_100,
             'query':query,
             'results':results}
    return render(request,'geomatic/documents.html',context)

@login_required
def video(request):
    vid=Video.objects.all()
    query=request.GET.get('q','')
    if query:
        queryset=(Q(description__icontains=query))
        results=Video.objects.filter(queryset).distinct()
    else:
        results=[] 
    context={'vid':vid,
             'query':query,
             'results':results}
    return render(request,'geomatic/video.html',context)


def software(request):
    soft=Software.objects.all()
    query=request.GET.get('q','')
    if query:
        queryset=(Q(id__icontains=query))
        results=Software.objects.filter(queryset).distinct()
    else:
        results=[] 
    context={'soft':soft,
             'query':query,
             'results':results}
    return render(request,'geomatic/software.html',context)


@login_required
def upload(request):
    form=UploadfilesForm()
    context={'form':form}
    if request.method=='POST':
        form=UploadfilesForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()

            return redirect('index')
        else:
            form=UploadfilesForm()    
    return render(request,'geomatic/upload.html',context)
