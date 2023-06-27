from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from apps.product.models import Product

from .utils import get_total, get_total_cleaned


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True)
    quantity = models.IntegerField(null=False, blank=False, verbose_name='Количество проданного товара:')
    discount = models.CharField(null=False, blank=True, default='0', max_length=5,
                                verbose_name='Размер скидки в процентах или в рублях, например: 10% или 250')
    customer_phone = models.CharField(max_length=20, null=True, blank=True,
                                      verbose_name='Номер телефона покупателя (опционально):')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи:')
    notes = models.TextField(blank=True, verbose_name='Комментарий к продаже:')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    @property
    def get_product_name(self):
        return self.product.name

    @property
    def get_total_score(self):
        return get_total(retail_price=self.product.retail_price,
                         quantity=self.quantity,
                         discount=self.discount
                         )

    @property
    def get_clean_total_score(self):
        return get_total_cleaned(retail_price=self.product.retail_price,
                                 purchase_price=self.product.purchase_price,
                                 quantity=self.quantity,
                                 discount=self.discount,
                                 )
