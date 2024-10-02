from django.views import generic
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView)
from django.contrib.auth.decorators import login_required 
from .models import Quote
from .forms import QuoteForm


# Create your views here 
    
class Quotes(ListView):
    template_name = "quote/quotes.html"
    model = Quote
    context_object_name = 'quotes'
    paginate_by = 4

class DetailQuote(DetailView):
    model = Quote
    template_name = 'quote_detail.html'

class AddQuote(CreateView):
    template_name = 'quote/add_quote.html'
    model = Quote
    form_class = QuoteForm
    success_url = '/quote/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddQuote, self).form_valid(form)

class EditQuote(UpdateView):
    model = Quote
    template_name = 'edit_quote.html'
    fields = ['content', 'author', 'source', 'category']
    success_url = '/quote/'

class DeleteQuote(DeleteView):
    model = Quote
    template_name = 'delete_quote.html'
    success_url = '/quote/'





