from django.urls import path
from .views import Quotes, AddQuote, QuoteDetailView, EditQuoteView

urlpatterns = [
    path('add/', AddQuote.as_view(), name='add_quote'),
    path('', Quotes.as_view(), name='quotes'),
    path('edit/<int:pk>/', EditQuoteView.as_view(), name='edit_quote'),
    path('<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
]
