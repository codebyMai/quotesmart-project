from django.urls import path
from . import views
from .views import QuoteList, AddQuote

urlpatterns = [
    path('', QuoteList.as_view(), name='quote'),
    path('add/', AddQuote.as_view(), name='add_quote'),
] 

