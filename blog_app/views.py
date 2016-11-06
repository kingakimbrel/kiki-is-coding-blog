from django.shortcuts import render
from .models import Post


def index(request):
    """The home page for blog./Show all posts."""
    posts = Post.objects.order_by('-date_added')
    context = {'posts': posts}

    return render(request, 'blog_app/index.html', context)


def view_post(request, post_id):
    blog_post = Post.objects.get(id=post_id)
    context = {'blog_post': blog_post}
    return render(request, 'blog_app/view_post.html', context)
