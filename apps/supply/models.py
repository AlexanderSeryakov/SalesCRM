from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Supply(models.Model):
    shipper = models.CharField(max_length=24, blank=False)
    shipper_phone = models.CharField(max_length=11, blank=True)
    shipper_buisnes = models.CharField(max_length=24, blank=True)
    shipper_address = models.CharField(max_length=48, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.JSONField()
    total_products = models.IntegerField(blank=False)
    comments = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.shipper
    
    def get_absolute_url(self):
        return reverse('supply_detail', kwargs={'pk': self.pk})



