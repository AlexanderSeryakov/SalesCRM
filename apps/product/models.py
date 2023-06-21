from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=512)
    purchase_price = models.FloatField(null=False, blank=False)
    retail_price = models.FloatField(null=False, blank=False)
    in_stock = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, null=True, blank=True)

    class Meta:
        ordering = ['-in_stock']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})
