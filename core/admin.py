from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
from .models import Snippet, Website, Page, Block, Section, Footer, Header, Aside, BlockInSection, ExternalLink

class OptimatronModelAdmin(admin.ModelAdmin):
    #change_list_template = "admin/change_list_filter_sidebar.html"
    pass


class OptimatronModelContentAdmin(OptimatronModelAdmin):
    list_display__active = ['is_active','is_active_value']
    list_display__dates = ['created_on_date', 'updated_on_date']
    list_display = list_display__active + list_display__dates

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


#@admin.register(ExternalLink)
#class ExternalLinkAdmin(OptimatronModelAdmin):
#    model = ExternalLink


class ExternalLinkInline(GenericTabularInline):
    model=ExternalLink
    fields = [ 'titre', 'url', 'link_text', 'icone']


@admin.register(Website)
class WebsiteAdmin(OptimatronModelContentAdmin):
    date_hierarchy = 'created_on'
    readonly_fields = ['created_on', 'updated_on']

    list_display = OptimatronModelContentAdmin.list_display__active\
        + ['nom', 'author']\
        + OptimatronModelContentAdmin.list_display__dates

    list_filter = OptimatronModelContentAdmin.list_filter + []
    inlines = [ExternalLinkInline,]


@admin.register(Page)
class PageAdmin(OptimatronModelAdmin):
    date_hierarchy = 'updated_on'
    filter_vertical = ['websites']


class BlockInSectionSectionInline(SortableInlineAdminMixin, admin.TabularInline):
    model = BlockInSection
    readonly_fields = ['nice_position', ]
    fields = ['position', 'nice_position', 'block' ]


class BlockInSectionBlockInline(admin.TabularInline):
    model = BlockInSection
    fields = [ 'section', 'position',]


@admin.register(Block)
class BlockAdmin(OptimatronModelContentAdmin ):
    date_hierarchy = 'updated_on'
    list_display = [] + OptimatronModelContentAdmin.list_display__active \
                   + [ 'nom', 'author'] \
                   + OptimatronModelContentAdmin.list_display__dates
    inlines = [ BlockInSectionBlockInline, ]


@admin.register(Section)
class SectionAdmin(OptimatronModelAdmin):
    #date_hierarchy = 'updated_on'
    fields = []
    list_display = ['nom']
    inlines = [ BlockInSectionSectionInline, ]
    #filter_horizontal = ('pages','blocks')


@admin.register(Header)
class HeaderAdmin(OptimatronModelAdmin):
    date_hierarchy = 'updated_on'

@admin.register(Aside)
class AsideAdmin(OptimatronModelAdmin):
    date_hierarchy = 'updated_on'

@admin.register(Footer)
class FooterAdmin(OptimatronModelAdmin):
    date_hierarchy = 'updated_on'
