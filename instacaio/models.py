from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey(
        to = User,
        on_delete = models.SET_NULL,
        null = True
    )
    imagem = models.ImageField(upload_to='posts')
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add = True)
    aprovado = models.BooleanField(default = False)
