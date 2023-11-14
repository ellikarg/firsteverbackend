from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    Category model, related to User and Post
    Changeable by the admin user
    """
    name = models.CharField(max_length=40, blank=False, default='')
    owner = models.ForeignKey(
        User,
        related_name='category',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name
