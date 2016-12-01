from django.db import models
from tinymce_4.fields import TinyMCEModelField
from author.decorators import with_author
from django.contrib.auth.models import User

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


class ContentBase(models.Model):
    is_active = models.BooleanField(default=1, verbose_name="Actif")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    #Both author & updated_by managed by django-author
    author = models.ForeignKey(User, related_name="%(class)s_author")
    updated_by = models.DateTimeField

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

    def __str__(self):
        return self.nom


class Website(ContentBase):
    nom = models.CharField(max_length=512)

    def __str__(self):
        return self.nom

    def created_on_small(self):
        return self.created_on.time()

class Page(ContentBase, CssAttributesMixin):
    titre = models.CharField(max_length=512)
    websites = models.ManyToManyField(Website, related_name="pages")

    def __str__(self):
        return self.titre

class Section(ContentBase, CssAttributesMixin):
    nom = models.CharField(max_length=512, blank=True)
    blocks = models.ManyToManyField("Block", related_name="section")
    pages = models.ManyToManyField("Page", related_name="sections")

    def __str__(self):
        return self.nom

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



