# Generated by Django 4.2.8 on 2024-03-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_comment_parent_comment_comment_top_level_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='article.tag'),
        ),
    ]
