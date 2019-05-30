from django.db import models
from datetime import datetime


class Item(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    deadline = models.DateTimeField()
    priorities = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    priority = models.CharField(max_length=1, choices=priorities, default='M')
    createdAt = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = 'items'

    def __str__(self):
        return self.title
