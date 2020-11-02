from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.author}: {self.content}'

