from django.db import models
from django.utils import timezone
form django.contrib.auth.models import User

class Post (models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft')
        ('published', 'Published'),
    )

    title = model.CharField(max_length=250)
    slung = models.SlungField(max_length = 250, unique_for_date='publish')
    author = models.ForeignKey(on_delete=models.CASCADE, related_name='blog_posts')

