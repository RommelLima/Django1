from django.shortcuts import render
from .models import Post


def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html',
             'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi',
             'Systemctl']

    list_post = Post.objects.all
    data = {'name': 'Curso de Django',
            'list_tecnology': lista,
            'posts': list_post }



    return render(request, 'index.html', data)