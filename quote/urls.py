from django.urls import path
from . import views
from .views import QuoteList

urlpatterns = [
    path('', QuoteList.as_view(), name='quote'),
] 

