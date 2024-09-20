from django.shortcuts import render
from django.views import generic
from .models import Quote

# Create your views here.
class Index(generic.ListView):
    queryset = Quote.objects.all()
    template_name = "home/index.html"
    
