from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    """Add Quote form""" 
    class Meta:
        model = Quote
        fields = ('content',
                  'author',
                  'source',
                  'category')
