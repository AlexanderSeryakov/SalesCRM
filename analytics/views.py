from django.http import HttpResponse
from sale.models import Sale


def home(request):
    sales = Sale.objects.filter(user_id=request.user.pk)
    return HttpResponse(f"Приветствую в разделе аналитики, {request.user} ! Всего сделано: {len(sales)} продаж.")
