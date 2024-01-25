from django.contrib import admin
from .models import (
    Article,
    Category,
    Tag,
    Author,
    Comment,
    ArticleContent,
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    list_display_links = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    list_display_links = ('title',)


class ArticleContentAdminTabularInline(admin.TabularInline):
    model = ArticleContent
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleContentAdminTabularInline]
    list_display = ('id', 'title', 'created_date', )
    search_fields = ('title', )
    list_filter = ('created_date', )
    list_display_links = ('title',)
    date_hierarchy = 'created_date'
    readonly_fields = ('created_date', 'slug')
    save_on_top = True
    filter_horizontal = ('tags',)
    # prepopulated_fields = {'slug': ('title',)}





@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'name', 'email', 'get_image', 'created_date', )
    search_fields = ('name', 'article__title')
    readonly_fields = ('created_date',)
    autocomplete_fields = ('article',)
