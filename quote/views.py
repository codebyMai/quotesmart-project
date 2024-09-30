from django.views import generic
from django.views.generic import (
    CreateView, ListView,)
from .models import Quote
from .forms import QuoteForm

# Create your views here 
    
class Quotes(ListView):
    #queryset = Quote.objects.filter(verified=True)
    template_name = "quote/quotes.html"
    model = Quote
    context_object_name = 'quotes'

class AddQuote(CreateView):
    template_name = 'quote/add_quote.html'
    model = Quote
    success_url = "/quote/"
    form_class = QuoteForm 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddQuote, self).form_valid(form)
