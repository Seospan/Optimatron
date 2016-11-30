from django.contrib import admin

# Register your models here.
from .models import Snippet, Website, Page, Block, Section, Footer, Header, Aside

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('titre', 'slug', 'pub_date')


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_on'
    #fieldsets = (
     #   (None, {
      #      'fields': ('nom', 'pages', 'author')
       # }),
    #)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_on'
    filter_vertical = ['websites']


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_on'


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    #date_hierarchy = 'updated_on'
    list_display = ['nom']
    filter_horizontal = ('pages','blocks')



@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_on'

@admin.register(Aside)
class AsideAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_on'

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_on'
