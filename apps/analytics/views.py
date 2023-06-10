from django.shortcuts import render

from apps.sale.models import Sale


def home(request):
    sales = Sale.objects.filter(user_id=request.user.pk)
    return render(request, 'analytics/base.html', {})
