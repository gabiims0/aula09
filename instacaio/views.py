from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from instacaio.forms import PostForm
from instacaio.models import Post


def inicio(request):
    posts = Post.objects.filter(aprovado = True)
    return render(request, 'inicio.html', {
        'posts': posts
    })

# Create your views here.
@login_required(login_url='/contas/login')
def criar_post(request:HttpRequest):
    if (request.method == "POST"):
        formulario = PostForm(request.POST, request.FILES)
        if (formulario.is_valid):
            post:Post = formulario.save(commit = False)
            post.autor = request.user
        if request.user.is_staff:
            post.aprovado = True
            post.save()
            return redirect("inicio")
    else:
        formulario = PostForm()
    return render(request, 'postar.html', {
        "formulario": formulario
    })