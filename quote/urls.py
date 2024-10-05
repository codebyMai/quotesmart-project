from django.urls import path
from .views import Quotes, AddQuote, DetailQuote, EditQuote, DeleteQuote
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('add/', login_required(AddQuote.as_view()), name='add_quote'),
    path('', login_required(Quotes.as_view()), name='quotes'),
    path('quote/edit/<int:pk>/', login_required(EditQuote.as_view()),
         name='edit-quote'),
    path('quote/<int:pk>/', login_required(DetailQuote.as_view()),
         name='detail-quote'),
    path('quote/<int:pk>/delete', login_required(DeleteQuote.as_view()),
         name='delete-quote'),
]
