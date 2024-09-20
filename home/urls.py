from django.urls import path
#from . import views
from  .views import Index

urlpatterns = [
    #path('', views.QuoteList.as_view(), name='home'),
    path('', Index.as_view(), name='home')
]
