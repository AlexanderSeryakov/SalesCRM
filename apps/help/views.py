from django.http import HttpResponse
from django.shortcuts import render


def help_home(request):
    return HttpResponse('200, OK')
