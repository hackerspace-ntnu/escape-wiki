from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=4000, blank=True)
    code = models.CharField(max_length=20)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Hint(Article):
    hardhint = models.TextField(max_length=4000, blank=True)
    mediumhint = models.TextField(max_length=4000, blank=True)
    easyhint = models.TextField(max_length=4000, blank=True)
