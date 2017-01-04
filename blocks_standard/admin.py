from django.contrib import admin

# Register your models here.
from .models import BlockImage, BlockTexte
from core.admin import BlockAdmin

@admin.register(BlockImage)
class BlockImage(BlockAdmin):
    pass
