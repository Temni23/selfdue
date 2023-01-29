from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True, blank=True)
    is_published = models.BooleanField(default=True, blank=True)
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                            related_name='women')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('women:post', kwargs={'post_id': self.pk})
