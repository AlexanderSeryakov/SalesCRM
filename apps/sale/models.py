from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from apps.product.models import Product


class TestModel(models.Model):
    string = models.CharField(max_length=256)


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    discount = models.FloatField(default=0, null=True, blank=True)
    customer_name = models.CharField(max_length=512)
    customer_phone = models.CharField(max_length=20)
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
        total = self.product.price * self.quantity
        return total - total * (self.discount / 100)
