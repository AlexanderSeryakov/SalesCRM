from django.db import models


class Sale(models.Model):
    product_name = models.CharField(max_length=256)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0, null=True, blank=True)
    customer_name = models.CharField(max_length=512)
    customer_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return self.pk

    @property
    def get_total_price(self):
        total = self.price * self.quantity
        return total - total * (self.discount / 100)



