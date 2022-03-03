from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def paginaInicial(request):
    return render(request,'inicio/index.html')