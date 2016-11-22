from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Snippet(models.Model):
    titre = models.CharField(max_length=320)
    slug = models.SlugField(unique=True,primary_key=True)
    contenu = HTMLField()
    pub_date = models.DateTimeField('date de publication')

    def __str__(self):
        return self.titre