from django.shortcuts import render, get_object_or_404
from .models import Experience, BlogPost, Skill, Formacao, SobreMim, Projeto, Apresentacao


def home(request):
    apresentacao = Apresentacao.objects.first()  # <-- novo
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    formacoes = Formacao.objects.all()
    sobre = SobreMim.objects.first()
    projetos = Projeto.objects.all()

    return render(request, 'index.html', {
        'apresentacao': apresentacao,  # <-- novo
        'experiences': experiences,
        'skills': skills,
        'formacoes': formacoes,
        'sobre': sobre,
        'projetos': projetos,
    })


def blog(request):
    posts = BlogPost.objects.all().order_by('-data_publicacao')
    return render(request, 'blog.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'post_detail.html', {'post': post})
