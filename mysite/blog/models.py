from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post (models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft')
        ('published', 'Published'),
    )

    title = model.CharField(max_length=250)
    slung = models.SlungField(max_length = 250, unique_for_date='publish')
    author = models.ForeignKey(on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=true)
    status = models.CharField(max_length=10, choice=STATUS_CHOICES, default='draft')

    class Meta:
         ordering = ('-publish',)

    def __str__(self):
        return self.title

