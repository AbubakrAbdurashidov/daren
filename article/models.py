
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/authors')
    bio = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='author')
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(editable=False, null=True, blank=True)
    image = models.ImageField(upload_to='media/article', null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArticleContent(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='ArticleContent')
    content = RichTextField(null=True, blank=True)
    is_quote = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.article.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255,  null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='media/comments', null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='parent')
    top_level_comment = models.IntegerField(null=True, blank=True)

    @property
    def children(instance, *args, **kwargs):
        if not instance.top_level_comment:
            child = Comment.objects.filter(top_level_comment=instance.id).order_by('-id')
            return child
        else:
            return None

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="50" height="50" /></a>')
        return '-'


def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent_comment:
        if instance.parent_comment.top_level_comment:
            instance.top_level_comment = instance.parent_comment.top_level_comment
        else:
            instance.top_level_comment = instance.parent_comment.id


def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + "-" + str(timezone.now().date()))


pre_save.connect(article_pre_save, sender=Article)
pre_save.connect(comment_pre_save, sender=Comment)
