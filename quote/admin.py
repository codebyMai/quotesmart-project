from django.contrib import admin
from .models import Quote


# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "author",
        "source",
        "category",
        "verified",
        "created_on",
    )
    list_filter = ("category",)

