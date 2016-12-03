from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from blog_app.forms import CommentForm
from blog_app.static.functions.queries import *
from .models import Comment


def index(request):
    """The home page for blog./Show all posts."""
    posts = Post.objects.annotate(ccount=Count('comments')).order_by('-date_added')
    last_posts = get_latest_post()
    archive = get_archive()
    context = {'posts': posts, 'l_posts': last_posts, 'archive_tree': archive}

    return render(request, 'blog_app/index.html', context)


def view_post(request, post_id):
    """View selected post."""
    blog_post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    last_posts = get_latest_post()
    archive = get_archive()
    context = {'blog_post': blog_post, 'comments': comments, 'l_posts': last_posts, 'archive_tree': archive}
    return render(request, 'blog_app/view_post.html', context)


def get_posts(request, year, month):
    t_posts = Post.objects.filter(date_added__year=year, date_added__month=month)
    context = {'t_posts': t_posts}
    return render(request, 'blog_app/archive_posts.html', context)


def add_new_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = int(request.POST['blog_post_id'])
            post = Post.objects.get(id=post_id)
            new_comment_entry = form.save(commit=False)
            new_comment_entry.post = post
            new_comment_entry.save()
            comments = Comment.objects.filter(post_id=post_id)
            html = render_to_string('blog_app/comments.html', {'comments': comments})
            return HttpResponse(html)

    return HttpResponse(
        content="",
        content_type="application/json",
        status=400
    )
