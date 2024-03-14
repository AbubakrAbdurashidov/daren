from rest_framework import serializers
from article.models import Article
from article.models import Author, Category, Tag, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'image', 'bio']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'category', 'slug', 'image', 'tags', 'modified_date', 'created_date']


class ArticlePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['author', 'title', 'category', 'image', 'tags']


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'article', 'image', 'name', 'email', 'created_date', 'message', 'parent_comment', 'top_level_comment']


class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article', 'name', 'image', 'email', 'message', 'parent_comment', 'top_level_comment']
