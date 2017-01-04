from django.db import models
from core.models import Block
# Create your models here.

class BlockImage(Block):
    image_name = models.CharField(max_length=256)


class BlockTexte(Block):
    texte = models.CharField(max_length=512)