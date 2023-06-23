from django.http import Http404

from .models import Sale


class UserSalePermissionMixin:
    """
    Mixin for checking user permission to manage the current Sale-object.
    Override get_object method from django SingleObjectMixin.

    if user does not have permission, returned Http404
    else returned Sale-object, which we requested by <int:pk>.

    Use this Mixin only if your view take <int:pk>.

    You can call this method in subclass and hand over your queryset.
    Default queryset will be `Sale.objects.filter(user_id=self.request.user.pk).select_related('product')`
    """
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)

        if queryset is None:
            queryset = Sale.objects.filter(user_id=self.request.user.pk).select_related('product')

        if pk is not None:
            queryset = queryset.filter(pk=pk)

        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                ('Error. Please, enter correct ID!')
            )
        return obj
