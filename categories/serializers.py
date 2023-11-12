from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'post']
