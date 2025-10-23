from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):  # type: ignore
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=200)
    path = models.FileField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="images"
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
