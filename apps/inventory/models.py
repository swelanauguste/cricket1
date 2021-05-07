from django.db import models
from django.urls.base import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='Inventory', default=1)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    desc = models.TextField("details", blank=True)

    def get_absolute_url(self):
        return reverse("inventory:detail", kwargs={"pk": self.pk})

    def get_asset_value(self):
        return self.price * self.count

    def __str__(self):
        return self.name
