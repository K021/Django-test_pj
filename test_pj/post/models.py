from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
