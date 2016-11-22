from django.contrib import admin

# Register your models here.
from .models import Snippet

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('titre', 'slug', 'pub_date')