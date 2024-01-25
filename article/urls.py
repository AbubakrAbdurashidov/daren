from django.urls import path
from .views import (
    article_view,
    article_detail,
    article_category,
    article_archive,
)

app_name = 'article'

urlpatterns = [
    path('', article_view,  name='view'),
    path('article/detail/<slug:slug>/', article_detail, name='detail'),
    path('article/category/', article_category, name='category'),
    path('article/archive/', article_archive, name='archive'),
]