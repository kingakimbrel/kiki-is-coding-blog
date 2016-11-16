"""Defines URL patterns for blog_app"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Detail page for single topic
    url(r'^view_post/(?P<post_id>\d+)/$', views.view_post, name='view_post'),
    url(r'^get_latest_post/$', views.get_latest_post, name='get_latest_post'),
    url(r'^get_archive/$', views.get_archive, name='get_archive'),
    url(r'^get_posts/(?P<year>\d+)/(?P<month>\d+)/$', views.get_posts, name='get_posts'),
]
