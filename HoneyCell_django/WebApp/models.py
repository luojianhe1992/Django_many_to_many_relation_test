from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Publication(models.Model):
    publication_name = models.CharField(max_length=100)
    publication_time_created = models.DateTimeField(auto_now_add=True)
    publication_time_changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" %(self.publication_name)

    class Meta:
        ordering = ('publication_name', )


class Article(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    publications = models.ManyToManyField(Publication)
    article_time_created = models.DateTimeField(auto_now_add=True)
    article_time_changed = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return "%s, %s, %s" %(self.headline, self.content, self.publications)

    class Meta:
        ordering = ('headline', )


class FavoritePublication(models.Model):
    user = models.ForeignKey(User)
    publication = models.ForeignKey(Publication)
    favorite_publication_time_created = models.DateTimeField(auto_now_add=True)
    favorite_publication_time_changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s like %s" %(self.user, self.publication)

    class Meta:
        ordering = ('user', )


class FavoriteArticle(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    favorite_article_time_created = models.DateTimeField(auto_now_add=True)
    favorite_article_time_changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s like %s" %(self.user, self.article)

    class Meta:
        ordering = ('user', )

