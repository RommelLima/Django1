from django.shortcuts import render


def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html',
             'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi',
             'Systemctl']
    data = {'name': 'Curso de Django', 'list_tecnology': lista}
    return render(request, 'index.html', data)