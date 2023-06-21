from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from apps.product.models import Product


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True)
    quantity = models.IntegerField(null=False, blank=False)
    discount = models.IntegerField(null=False, blank=False)
    customer_phone = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    @property
    def get_total_score(self):
        total = self.product.retail_price * self.quantity
        return total - total * (self.discount / 100)

    @property
    def get_clean_total_score(self):
        total = self.product.purchase_price * self.quantity
        return self.get_total_score - total
