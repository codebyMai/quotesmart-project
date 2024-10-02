from django.urls import path
from .views import Quotes, AddQuote, DetailQuote, EditQuote

urlpatterns = [
    path('add/', AddQuote.as_view(), name='add_quote'),
    path('', Quotes.as_view(), name='quotes'),
    path('quote/edit/<int:pk>/', EditQuote.as_view(), name='edit-quote'),
    path('quote/<int:pk>/', DetailQuote.as_view(), name='detail-quote'),
]
