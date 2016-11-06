"""Defines URL patterns for blog_app"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Detail page for single topic
    url(r'^view_post/(?P<post_id>\d+)/$', views.view_post, name='view_post'),
]
