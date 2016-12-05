from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

# Register your models here.
from .models import Snippet, Website, Page, Block, Section, Footer, Header, Aside

class OptimatronModelAdmin(admin.ModelAdmin):
    #change_list_template = "admin/change_list_filter_sidebar.html"
    pass


class OptimatronModelContentAdmin(OptimatronModelAdmin):
    list_display_before = ['is_active','is_active_value']
    list_display_after = ['created_on_date', 'updated_on_date']
    list_display =  list_display_before+list_display_after
    list_display_links = ['nom']

    list_filter = ['author', 'created_on', 'updated_on']
    list_editable = ['is_active','author']

    def created_on_date(self, obj):
        return obj.created_on.strftime("%d %b %Y")
    created_on_date.admin_order_field = 'created_on'
    created_on_date.short_description = 'Created_on date'

    def updated_on_date(self, obj):
        return obj.updated_on.strftime("%d %b %Y")
    updated_on_date.admin_order_field = 'updated_on'
    updated_on_date.short_description = 'Updated_on date'


@admin.register(Snippet)
class SnippetAdmin(OptimatronModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('titre', 'slug', 'pub_date')

@admin.register(Website)
class WebsiteAdmin(OptimatronModelContentAdmin):
    date_hierarchy = 'created_on'
    readonly_fields = ['created_on', 'updated_on']

    list_display = OptimatronModelContentAdmin.list_display_before\
        + ['nom', 'author']\
        + OptimatronModelContentAdmin.list_display_after

    list_filter = OptimatronModelContentAdmin.list_filter + []


@admin.register(Page)
class PageAdmin(OptimatronModelAdmin):
    date_hierarchy = 'updated_on'
    filter_vertical = ['websites']


@admin.register(Block)
class BlockAdmin(OptimatronModelAdmin):
    date_hierarchy = 'updated_on'


@admin.register(Section)
class SectionAdmin(OptimatronModelAdmin):
    #date_hierarchy = 'updated_on'
    list_display = ['nom']
    filter_horizontal = ('pages','blocks')



@admin.register(Header)
class HeaderAdmin(OptimatronModelAdmin):
    date_hierarchy = 'updated_on'

@admin.register(Aside)
class AsideAdmin(OptimatronModelAdmin):
    date_hierarchy = 'updated_on'

@admin.register(Footer)
class FooterAdmin(OptimatronModelAdmin):
    date_hierarchy = 'updated_on'
