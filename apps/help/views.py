from django.shortcuts import render


def help_home(request):
    return render(request, 'help/help_page.html', context={'title': 'Помощь'})


def about_project(request):
    return render(request, 'help/about.html', context={'title': 'О проекте'})


def help_license(request):
    return render(request, 'help/license.html', context={'title': 'Лицензия'})
