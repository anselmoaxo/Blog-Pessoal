# Generated by Django 5.0 on 2023-12-20 03:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_update_at_post_updated_at_post_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_in_post_content',
            field=models.BooleanField(default=True, help_text='Se marcado, exibirá a capa dentro do post.'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Este campo precisará estar marcado para o post ser exibido publicamente.'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, default='', to='blog.tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
