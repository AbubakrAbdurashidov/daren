from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ArticleSerializer, ArticlePostSerializer, CommentSerializer, CommentPostSerializer, CategorySerializer, TagSerializer
from ..models import Article, Comment, Category, Tag


@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(['POST'])
def article_create(request):
    serializer = ArticlePostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        success_serializer = ArticleSerializer(serializer.data)
        return Response(success_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def article_list_create(request):
    if request.method == 'POST':
        serializer = ArticlePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            success_serializer = ArticleSerializer(serializer.data)
            return Response(success_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    articles = Article.objects.all()
    serializer = ArticlePostSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    data = {
        'success': True,
        'message': 'Article has been deleted!'
    }
    return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def article_update(request, slug):
    article = get_object_or_404(Article, slug=slug)
    data = request.data
    partial = False
    if request.method == 'PATCH':
        partial = True
    serializer = ArticleSerializer(data=data, instance=article, partial=partial)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def comment_list(request):
    comment = Comment.objects.all()
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def comment_create(request):
    if request.method == 'POST':
        serializer = CommentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            success_serializer = CommentSerializer(serializer.data)
            return Response(success_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_detail(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'PATCH'])
def category_list_page(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def tag_list_page(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


