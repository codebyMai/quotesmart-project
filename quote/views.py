from django.shortcuts import render
from django.views import generic, CreateView
from .models import Quote

# Create your views here 
    
class QuoteList(generic.ListView):
    queryset = Quote.objects.filter(verified=True)
    template_name = "quote/quotes.html"
    paginate_by = 6 

class AddQuote(CreateView):
    template_name = 'quote/add_quote.html'
    model = Quote
