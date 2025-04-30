from rest_framework import serializers
from .models import Post, Author, Tag

# ✅ Tag serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

# ✅ Author serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'profile_picture']

# ✅ Used for reading posts (GET requests)
class PostReadSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'image', 'author', 'tags', 'published_at']

# ✅ Used for creating/editing posts (POST/PUT requests)
class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'image', 'author', 'tags', 'published_at']
