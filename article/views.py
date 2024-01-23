from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Tag
from .forms import CommentForm
from django.core.paginator import Paginator


def article_view(request):
    page = request.GET.get('page')
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    q = request.GET.get('q')
    tags = Tag.objects.all()
    banner_articles = Article.objects.order_by('-id')[:2]
    last_articles = Article.objects.order_by('-id')[:3]
    object_articles = Article.objects.all()[:3]
    categories = Category.objects.all()
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
        'tags': tags,
        'categories': categories,
        'last_articles': last_articles,
        'object': object_articles
    }
    return render(request, 'article/index.html', ctx)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    articles = Article.objects.order_by('-id')
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    q = request.GET.get('q')
    author = request.GET.get('author')
    categories = Category.objects.all()
    last_articles = Article.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    form = CommentForm()
    if q:
        articles = articles.filter(title__icontains=q)
    if cat:
        articles = articles.filter(category__title__exact=cat)

    if tag:
        articles = articles.filter(tags__title__exact=tag)

    if author:
        articles = articles.filter(author__name__exact=author)
    print(author)
    if request.method == 'POST':
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.article = article
            obj.save()
            return redirect('.#redirect_window')
    ctx = {
        'object_list': articles,
        'object': article,
        'form': form,
        'author': author,
        'tags': tags,
        'categories': categories,
        'last_articles': last_articles

    }
    return render(request, 'article/single-blog.html', ctx)


def article_category(request):
    articles = Article.objects.order_by('-id')
    last_articles = Article.objects.order_by('-id')[:3]
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    tags = Tag.objects.all()
    q = request.GET.get('q')
    categories = Category.objects.all()
    if q:
        articles = articles.filter(title__icontains=q)
    if cat:
        articles = articles.filter(category__title__exact=cat)

    if tag:
        articles = articles.filter(tags__title__exact=tag)
    ctx = {
        'object_list': articles,
        'tags': tags,
        'last_articles': last_articles,
        'categories': categories
    }
    return render(request, 'article/category.html', ctx)


def article_archive(request):
    articles = Article.objects.order_by('-id')
    last_articles = Article.objects.order_by('-id')[:3]
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    if q:
        articles = articles.filter(title__icontains=q)
    if cat:
        articles = articles.filter(category__title__exact=cat)

    if tag:
        articles = articles.filter(tags__title__exact=tag)

    ctx = {
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