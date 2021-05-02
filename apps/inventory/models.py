from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='Inventory')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    desc = models.TextField("description", blank=True)

    def __str__(self):
        return self.name
