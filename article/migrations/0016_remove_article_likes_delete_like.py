# Generated by Django 4.2.8 on 2024-01-25 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_alter_like_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]