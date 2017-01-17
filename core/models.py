from django.db import models
from tinymce_4.fields import TinyMCEModelField
from author.decorators import with_author
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from multiselectfield import MultiSelectField

# Create your models here.

class Snippet(models.Model):
    titre = models.CharField(max_length=320)
    slug = models.SlugField(unique=True)
    contenu = TinyMCEModelField('Contenu')
    pub_date = models.DateTimeField('date de publication')

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("snippet-detail", args=[str(self.pk)])


class ExternalLink(models.Model):
    LINK_ICONS_CHOICES = (
        ('Réseaux sociaux',(
                ("fb.jpg", 'Facebook'),
                ("twitter.jpg", 'Twitter'),
                ("linkedin.jpg", 'Linkedin'),
            )
        ),
        ('Autres',(
                ("mail.jpg", 'Mail'),
            )
        )
    )

    titre = models.CharField(max_length=128, blank=True, null=True)
    url = models.URLField()
    link_text = models.CharField(max_length=256)
    icone =  models.CharField(
        max_length=128,
        choices=LINK_ICONS_CHOICES,
        default='fb.jpg',
    )
    #Generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.titre


class ContentBase(models.Model):
    is_active = models.BooleanField(default=1, verbose_name="Actif")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #Both author & updated_by managed by django-author
    author = models.ForeignKey(User, related_name="%(class)s_author", blank=True, null=True, on_delete=models.SET(1))
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

    def is_active_value(self):
        return self.is_active
    is_active_value.boolean = True


class CssAttributesMixin(models.Model):
    css_class = models.CharField(max_length=256, verbose_name="CSS classes", blank=True)
    css_id = models.CharField(max_length=128, verbose_name="CDD unique id", blank=True)
    css_inline = models.CharField(max_length=1200, verbose_name="CSS en ligne", blank=True)

    class Meta:
        abstract = True


class Website(ContentBase):
    nom = models.CharField(max_length=512)
    favicon = models.ImageField(upload_to="favicon", null=True, blank=True)
    icone = models.ImageField(upload_to="icone", null=True, blank=True)
    external_links = GenericRelation(ExternalLink)
    #external_links = models.ManyToManyField(ExternalLink, related_name=u"website", verbose_name = u"External Links" )
    #menu = models.ForeignKey(Tree, blank=True, null=True)
    #test = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nom

    def created_on_small(self):
        return self.created_on.time()


class Page(ContentBase, CssAttributesMixin):
    titre = models.CharField(max_length=512)
    websites = models.ManyToManyField(Website, related_name="pages")
    css_displayAside = models.BooleanField(default=False)
    css_displayHeader = models.BooleanField(default=True)
    css_displayFooter = models.BooleanField(default=True)

    def __str__(self):
        return self.titre


class Section(ContentBase, CssAttributesMixin):
    TITLE_TYPE_CHOICES = (
        ("H2", "h2"),
        ("H3", "h3"),
    )
    TITLE_CLASS_CHOICES = (
        ("Classe1","Classe 1"),
        ("Classe2","Classe 2"),
        ("Classe3","Classe 3"),
    )
    nom = models.CharField(max_length=512, null=True)
    css_haswrapper = models.BooleanField(default=False)
    #blocks = models.ManyToManyField("Block", related_name="section", through="BlockInSection")
    pages = models.ManyToManyField("Page", related_name="sections")
    titre = models.CharField(max_length=256)
    title_type = models.CharField(max_length=16, choices=TITLE_TYPE_CHOICES, verbose_name="Type de titre")
    classe_titre = MultiSelectField(choices=TITLE_CLASS_CHOICES, max_choices=3, max_length=64, null=True, blank=True, verbose_name="Type de titre")

    def __str__(self):
        return self.nom


class BlockInSection(models.Model):
    section = models.ForeignKey("Section", on_delete=models.CASCADE)
    block = models.ForeignKey("Block", on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(default=0, blank=False, null=False, verbose_name="Position of block in section")

    def nice_position(self):
        return self.position
    nice_position.short_description = "Position du block"

    class Meta(object):
        ordering = ('position',)


class Block(ContentBase, CssAttributesMixin):
    BLOC_FORMAT_CHOICES = (
        ("FULL", "Full width"),
        ("HALF", "Half width"),
        ("THIRD", "One third"),
        ("FOURTH", "One fourth"),
        ("2FOURTH", "Two fourth"),
        ("3FOURTH", "Three fourth"),
        ("FIFTH", "One fifth"),
    )
    nom = models.CharField(max_length=512)
    format = models.CharField(max_length=32, choices=BLOC_FORMAT_CHOICES, verbose_name="Format du bloc")
    #position = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    #sections = models.ForeignKey(Section, related_name="Blocks", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nom

    #class Meta(object):
    #    ordering = ('position',)


class Footer(ContentBase):
    blocks = models.ManyToManyField(Block, related_name="footer")
    website = models.ForeignKey(Website, related_name="footer", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Footer - "+self.website.nom

class Header(ContentBase):
    blocks = models.ManyToManyField(Block, related_name="header")
    website = models.ForeignKey(Website, related_name="header", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Header - "+self.website.nom

class Aside(ContentBase):
    blocks = models.ManyToManyField(Block, related_name="aside")
    website = models.ForeignKey(Website, related_name="aside", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Aside - "+self.website.nom



