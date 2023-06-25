from django.shortcuts import render


def help_home(request):
    return render(request, 'help/help_page.html', context={'title': 'Помощь'})


def about_project(request):
    return render(request, 'help/about.html', context={'title': 'О проекте'})
