from django import forms

from instacaio.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['data_postagem', 'autor', 'aprovado']