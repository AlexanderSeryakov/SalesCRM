from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=512, verbose_name='Наименование:')
    purchase_price = models.FloatField(null=False, blank=False, verbose_name='Закупочная стоимость:')
    retail_price = models.FloatField(null=False, blank=False, verbose_name='Розничная стоимость:')
    in_stock = models.PositiveIntegerField(null=False, blank=True, verbose_name='Количество товара:')
    notes = models.TextField(blank=True, null=True, verbose_name='Описание:')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, null=True, blank=True)

    class Meta:
        ordering = ['-in_stock']

    def __str__(self):
        return self.name

    def get_product_name(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})
