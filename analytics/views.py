from django.http import HttpResponse
from django.shortcuts import render

from sale.models import Sale


def home(request):
    sales = Sale.objects.filter(user_id=request.user.pk)
    return render(request, 'analytics/base.html', {})
