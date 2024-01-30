from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Tag, Comment
from .forms import CommentForm
from django.core.paginator import Paginator
from django.contrib import messages


def article_view(request):
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    q = request.GET.get('q')
    tags = Tag.objects.all()
    banner_articles = Article.objects.order_by('-id')[:1]
    banner_article = Article.objects.all()[:1]
    last_articles = Article.objects.order_by('-id')[:3]
    object_articles = Article.objects.all()[:3]
    categories = Category.objects.all()
    bottom_articles = Article.objects.order_by('-id')[:6]
    articles = Article.objects.order_by('-id')
    if q:
        articles = articles.filter(title__icontains=q)
    if cat:
        articles = articles.filter(category__title__exact=cat)

    if tag:
        articles = articles.filter(tags__title__exact=tag)

    ctx = {
        'object_list': articles,
        'banner_articles': banner_articles,
        'banner_article': banner_article,
        'tags': tags,
        'categories': categories,
        'bottom_articles': bottom_articles,
        'last_articles': last_articles,
        'object': object_articles
    }
    return render(request, 'article/index.html', ctx)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    user = request.user
    articles = Article.objects.order_by('-id')
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    q = request.GET.get('q')
    author = request.GET.get('author')
    categories = Category.objects.all()
    last_articles = Article.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    form = CommentForm()
    prev_item = Article.objects.filter(slug__lt=slug).last()
    parent_id = request.GET.get('p_id')
    next_item = Article.objects.filter(slug__gt=slug).first()
    if q:
        articles = articles.filter(title__icontains=q)
    if cat:
        articles = articles.filter(category__title__exact=cat)

    if tag:
        articles = articles.filter(tags__title__exact=tag)

    if author:
        articles = articles.filter(author__name=author)
    if request.method == 'POST':
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.article = article
            if parent_id:
                obj.parent_comment = Comment.objects.get(id=parent_id)
            obj.save()
            messages.success(request, 'Your message successfully sent')
            return redirect('.#redirect_window')

    ctx = {
        'object_list': articles,
        'object': article,
        'form': form,
        'author': author,
        'tags': tags,
        'user': user,
        'categories': categories,
        'last_articles': last_articles,
        'prev_item': prev_item,
        'next_item': next_item,

    }
    return render(request, 'article/single-blog.html', ctx)


def article_category(request):
    articles = Article.objects.order_by('-id')
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    last_articles = Article.objects.order_by('-id')[:3]
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    txt = "Categories"
    tags = Tag.objects.all()
    q = request.GET.get('q')
    categories = Category.objects.all()
    if q:
        page_obj = articles.filter(title__icontains=q)
    if cat:
        page_obj = articles.filter(category__title__exact=cat)
        txt = cat
    if tag:
        page_obj = articles.filter(tags__title__exact=tag)
    ctx = {
        'object_list': articles,
        'page_obj': page_obj,
        'tags': tags,
        'last_articles': last_articles,
        'categories': categories,
        'title': txt
    }
    return render(request, 'article/category.html', ctx)


def article_archive(request):
    articles = Article.objects.order_by('-id')
    paginator = Paginator(articles, 8)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    last_articles = Article.objects.order_by('-id')[:3]
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    if q:
        page_obj = articles.filter(title__icontains=q)
    if cat:
        page_obj = articles.filter(category__title__exact=cat)

    if tag:
        page_obj = articles.filter(tags__title__exact=tag)
    ctx = {
        'page_obj': page_obj,
        'object_list': articles,
        'tags': tags,
        'categories': categories,
        'last_articles': last_articles
    }
    return render(request, 'article/archive.html', ctx)


def article_navbar(request):
    articles = Article.objects.order_by('-id')
    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)
    ctx = {
        'object_list': articles,
    }
    return render(request, 'navbar.html', ctx)