from django.shortcuts import render
from django.views import generic

# Create your views here.
class Index(generic.ListView):
    template_name = "home/index.html"
    
  
from django.views.generic import ListView
from quote.models import Quote


class Index(ListView):
    template_name = 'home/index.html'
    model = Quote
    context_object_name = 'quotes'

    def get_queryset(self):
        return self.model.objects.all()[:3]

