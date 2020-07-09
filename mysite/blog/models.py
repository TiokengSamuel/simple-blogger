from django.db import models
from django.utils import timezone
form django.contrib.auth.models import User

class Post (models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft')
        ('published', 'Published'),
    )
