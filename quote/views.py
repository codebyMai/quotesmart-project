from django.views import generic
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView)
from django.contrib.auth.decorators import login_required   
from .models import Quote
from .forms import QuoteForm

# Create your views here 
    
class Quotes(ListView):
    #queryset = Quote.objects.filter(verified=True)
    template_name = "quote/quotes.html"
    model = Quote
    context_object_name = 'quotes'

class QuoteDetailView(DetailView):
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

class EditQuoteView(UpdateView):
    model = Quote
    template_name = 'edit_quote.html'
    fields = ['content', 'author', 'source', 'category']

"""
@login_required
def quote_remove(request, quote_id):
   item = Quote.objects.get(pk=quote_id)
   if request.user == item.user:
      Quote.objects.filter(id=quote_id).delete()
      return redirect('quotes')

def quote_edit(request, quote_id):
    quote = Quote.object.get(pk=quote_id)
    form = QuoteForm(request.POST or None, instance=quote)
    if form.is_valid():
        form.save()
        return redirect('quotes')

 @login_required
def quote_edit(request, quote_id):
   item = Quote.objects.get(pk=quote_id)
   if request.user == item.user:
      Quote.objects.filter(id=quote_id).edit()
      return redirect('quotes')"""

