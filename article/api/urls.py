from django.urls import path
from .views import (
    article_list,
    article_detail,
    article_create,
    article_list_create,
    article_delete,
    article_update,
    comment_list,
    comment_detail,
    comment_create,
    category_list_page,
    tag_list_page
)
app_name = 'api'


urlpatterns = [
    path('list/', article_list, name='article_list'),
    path('detail/<slug:slug>/', article_detail, name='detail'),
    path('create/', article_create, name='create'),
    path('list-create/', article_list_create, name='list-create'),
    path('delete/<slug:slug>/', article_delete, name='delete'),
    path('update/<slug:slug>/', article_update, name='update'),
    path('comments/', comment_list, name='comments'),
    path('comments/<int:pk>/', comment_detail, name='comment-detail'),
    path('comments/create/', comment_create, name='comment-create'),
    path('category_list/', category_list_page, name='category'),
    path('tag_list/', tag_list_page, name='tag'),
]