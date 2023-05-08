from django.shortcuts import render
from .models import Malumot
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        malumot = Malumot.objects.filter(Q(name__icontains=q)) 

    else:
        malumot = Malumot.objects.all().order_by('-id')
    return render(request,'list.html',{'malumot':malumot})
def home2(request):
    if 'q' in request.GET:
        q = request.GET['q']
        malumot = Malumot.objects.filter(Q(name__icontains=q)) 

    else:
        malumot = Malumot.objects.all().order_by('name')
    return render(request,'list.html',{'malumot':malumot})

