# Generated by Django 4.2.8 on 2024-01-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_author_category_tag_article_author_article_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/article'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(upload_to='media/authors'),
        ),
    ]
