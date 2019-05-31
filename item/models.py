from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    deadline = models.DateTimeField()
    PRIORITIES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    priority = models.CharField(max_length=1, choices=PRIORITIES, default='M')
    createdAt = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'items'

    def __str__(self):
        return self.title
