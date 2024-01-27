# Generated by Django 4.2.8 on 2024-01-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_alter_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/comments'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
