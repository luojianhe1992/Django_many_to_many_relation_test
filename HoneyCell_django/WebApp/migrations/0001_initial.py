# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 00:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('article_time_created', models.DateTimeField(auto_now_add=True)),
                ('article_time_changed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
        migrations.CreateModel(
            name='FavoriteArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_article_time_created', models.DateTimeField(auto_now_add=True)),
                ('favorite_article_time_changed', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='FavoritePublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_publication_time_created', models.DateTimeField(auto_now_add=True)),
                ('favorite_publication_time_changed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_name', models.CharField(max_length=100)),
                ('publication_time_created', models.DateTimeField(auto_now_add=True)),
                ('publication_time_changed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('publication_name',),
            },
        ),
        migrations.AddField(
            model_name='favoritepublication',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.Publication'),
        ),
        migrations.AddField(
            model_name='favoritepublication',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(to='WebApp.Publication'),
        ),
    ]
