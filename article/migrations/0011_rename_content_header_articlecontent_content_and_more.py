# Generated by Django 4.2.8 on 2024-01-23 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_remove_articlecontent_content_article_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlecontent',
            old_name='content_header',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
    ]
