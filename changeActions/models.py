from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ChangeAction(models.Model):
    category = models.ForeignKey(Category)
    image = models.ImageField(height_field=200, width_field=150, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    time = models.CharField(max_length=50)
    link = models.URLField(max_length=2000)
    linkText = models.CharField(max_length=250)

    def __str__(self):
        return self.name













