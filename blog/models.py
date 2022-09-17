from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Men(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField('publication', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='category')
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
