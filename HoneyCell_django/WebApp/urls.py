__author__ = 'jianheluo'

from django.conf.urls import include, url
from . import views


urlpatterns = [

    # empty url
    url(r'^$', 'WebApp.views.index', name='index'),

    # new argument 'template_name'
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'WebApp/login.html'}, name='login'),

    # url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'WebApp.views.my_logout', name='logout'),

    # registration is normal route
    url(r'^registration/$', 'WebApp.views.registration', name='registration'),

    # after login, show the message page to the user
    url(r'^message/$', 'WebApp.views.message', name='message'),

    # go to upload page
    url(r'^upload/$', 'WebApp.views.upload', name='upload'),

    # go to preprocess page
    url(r'preprocess/$', 'WebApp.views.preprocess', name='preprocess'),

    # go to visualization page
    url(r'visualization/$', 'WebApp.views.visualization', name='visualization'),

    # go to honeycell page
    url(r'honeycell/$', 'WebApp.views.honeycell', name='honeycell'),

    # go to honeycomb page
    url(r'honeycomb/$', 'WebApp.views.honeycomb', name='honeycomb'),

    # go to analytics page
    url(r'analytics/$', 'WebApp.views.analytics', name='analytics'),

    url(r'add_publication/$', 'WebApp.views.add_publication', name='add_publication'),

    url(r'show_publications/$', 'WebApp.views.show_publications', name='show_publications'),

    url(r'add_article/$', 'WebApp.views.add_article', name='add_article'),

    url(r'show_articles/$', 'WebApp.views.show_articles', name='show_articles'),

    url(r'add_favorite_publication/(?P<publication_id>\d+)$', 'WebApp.views.add_favorite_publication', name='add_favorite_publication'),

    url(r'cancel_favorite_publication/(?P<publication_id>\d+)$', 'WebApp.views.cancel_favorite_publication', name='cancel_favorite_publication'),

    url(r'add_favorite_article/(?P<article_id>\d+)$', 'WebApp.views.add_favorite_article', name='add_favorite_article'),

    url(r'cancel_favorite_article/(?P<article_id>\d+)$', 'WebApp.views.cancel_favorite_article', name='cancel_favorite_article'),

    url(r'show_favorite_publications/$', 'WebApp.views.show_favorite_publications', name='show_favorite_publications'),

    url(r'show_favorite_articles/$', 'WebApp.views.show_favorite_articles', name='show_favorite_articles'),

    url(r'add_article_using_modelform/$', 'WebApp.views.add_article_using_modelform', name='add_article_using_modelform'),

    url(r'publication_detail/(?P<publication_id>\d+)$', 'WebApp.views.publication_detail', name='publication_detail'),

    url(r'article_detail/(?P<article_id>\d+)$', 'WebApp.views.article_detail', name="article_detail"),

    url(r'add_article_to_publication/(?P<article_id>\d+)$', 'WebApp.views.add_article_to_publication', name='add_article_to_publication'),

    url(r'add_publication_to_article/(?P<publication_id>\d+)$', 'WebApp.views.add_publication_to_article', name='add_publication_to_article'),



]