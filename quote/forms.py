from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
  
    class Meta:
        model = Quote
        fields = ('content',
                  'author',
                  'source',
                  'category')
        