from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance with default image
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=160, null=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_i2ll5s', blank=True
    )
    category = models.ForeignKey(
        Category, related_name='category',
        on_delete=models.SET_NULL, null=True, default=None
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
