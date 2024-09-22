from django.contrib import admin
from .models import Quote
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Quote)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('content', 'author', 'source', 'verified')
    search_fields = ['verified']
    list_filter = ('verified',)
    summernote_fields = ('content',)

# Register your models here.

