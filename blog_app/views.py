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
    blog_post = Post.objects.get(id=post_id)
    context = {'blog_post': blog_post}
    return render(request, 'blog_app/view_post.html', context)
