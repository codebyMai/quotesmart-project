from django.urls import path
from . import views
from .views import Quotes, AddQuote

urlpatterns = [
    #path('', Quotes.as_view(), name='quotes'),
    path('quote/', Quotes.as_view(), name= 'quotes'),
    path('add/', AddQuote.as_view(), name='add_quote'),
] 

