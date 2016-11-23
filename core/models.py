from django.db import models
from tinymce_4.fields import TinyMCEModelField

# Create your models here.

class Snippet(models.Model):
    titre = models.CharField(max_length=320)
    slug = models.SlugField(unique=True)
    contenu = TinyMCEModelField('Contenu')
    pub_date = models.DateTimeField('date de publication')

    def __str__(self):
        return self.titre