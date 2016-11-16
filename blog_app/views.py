from django.shortcuts import render
from .models import Post
from blog_app.static.functions.queries import *


def index(request):
    """The home page for blog./Show all posts."""
    posts = Post.objects.order_by('-date_added')
    last_posts = get_latest_post()
    archive = get_archive()
    context = {'posts': posts, 'l_posts': last_posts, 'archive_tree': archive}

    return render(request, 'blog_app/index.html', context)


def view_post(request, post_id):
    """View selected post."""
    blog_post = Post.objects.get(id=post_id)
    last_posts = get_latest_post()
    archive = get_archive()
    context = {'blog_post': blog_post, 'l_posts': last_posts, 'archive_tree': archive}
    return render(request, 'blog_app/view_post.html', context)


def get_posts(request, year, month):
    t_posts = Post.objects.filter(date_added__year=year, date_added__month=month)
    context = {'t_posts': t_posts}
    return render(request, 'blog_app/archive_posts.html', context)
