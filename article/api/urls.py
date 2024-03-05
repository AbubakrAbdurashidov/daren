from django.urls import path
from .views import (
    article_list,
    article_detail,
    article_create,
    article_list_create,
)
app_name = 'api'


urlpatterns = [
    path('list/', article_list, name='article_list'),
    path('detail/<slug:slug>/', article_detail, name='detail'),
    path('create/', article_create, name='create'),
    path('list-create/', article_list_create, name='list-create'),
]