from django.db import models

# Create your models here.
class Listinha(models.Model):
    title = models.CharField(max_length=25)
    descricao = models.CharField(max_length=120)
    imagem = models.ImageField(upload_to="listinha/covers/%Y/%m/%d", blank=True, default="")
