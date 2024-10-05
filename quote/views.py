from django.views import generic
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView)


from .models import Quote
from .forms import QuoteForm

# Create your views here


class Quotes(ListView):
    """List of quotes view"""
    template_name = "quote/quotes.html"
    model = Quote
    context_object_name = 'quotes'
    paginate_by = 4


class DetailQuote(DetailView):
    """Detailed quote view"""
    model = Quote
    template_name = 'quote_detail.html'


class AddQuote(CreateView):
    """Add quote view"""
    template_name = 'quote/add_quote.html'
    model = Quote
    form_class = QuoteForm
    success_url = '/quote/'
    """Asign added_by to logged in user"""
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(AddQuote, self).form_valid(form)


class EditQuote(UpdateView):
    """Edit Quote"""
    model = Quote
    template_name = 'edit_quote.html'
    fields = ['content', 'author', 'source', 'category']
    success_url = '/quote/'


class DeleteQuote(DeleteView):
    """Delete Quote"""
    model = Quote
    template_name = 'delete_quote.html'
    success_url = '/quote/'





