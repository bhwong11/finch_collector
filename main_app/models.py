from django.db import models

# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100, default='NA')
    img = models.CharField(max_length=500)
    cool = models.BooleanField(default=True)
    color = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
