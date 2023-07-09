from django.shortcuts import render


def error_404_view(request, exception):
    return render(request, 'common/404.html', {'title': 'Ошибка'})
