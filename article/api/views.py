from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ArticleSerializer, ArticlePostSerializer
from ..models import Article


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