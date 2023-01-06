from django.db import models


class New(models.Model):
    CLASS_SPORTS = 'S'
    CLASS_HEALTH = 'H'
    CLASS_POLITICS = 'P'
    CLASS_ECONOMICS = 'E'
    CLASS_TECHNOLOGY = 'T'
    CLASS_CHOICES = [
        (CLASS_SPORTS, 'Sports'),
        (CLASS_HEALTH, 'Health'),
        (CLASS_POLITICS, 'Politics'),
        (CLASS_ECONOMICS, 'Economics'),
        (CLASS_TECHNOLOGY, 'Technology'),
    ]
    category = models.CharField(max_length=1, choices=CLASS_CHOICES)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} -- {self.title} -- {self.category}"
