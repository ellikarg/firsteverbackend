from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Category(models.Model):
    """
    Category model, related to User and Post
    Changeable by the admin user
    """
    name = models.CharField(max_length=40, blank=False, default='')
    owner = models.ForeignKey(
        User,
        related_name='categories',
        on_delete=models.CASCADE)
    posts = models.ManyToManyField(
        Post,
        related_name='categories',
        blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
