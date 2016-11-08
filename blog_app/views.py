from django.shortcuts import render
from .models import Post, ArchiveNode


def index(request):
    """The home page for blog./Show all posts."""
    posts = Post.objects.order_by('-date_added')
    context = {'posts': posts}

    return render(request, 'blog_app/index.html', context)


def view_post(request, post_id):
    blog_post = Post.objects.get(id=post_id)
    context = {'blog_post': blog_post}
    return render(request, 'blog_app/view_post.html', context)


def get_latest_post(request):
    last5posts = Post.objects.defer("text").order_by('-date_added')[:5]
    context = {'l_posts': last5posts}
    return render(request, 'blog_app/latestPosts.html', context)


def get_archive(request):
    all_posts = Post.objects.defer("text").order_by('-date_added')

    archive = []
    i = 0

    while i < len(all_posts):
        current_year = all_posts[i].date_added.year
        year_node = ArchiveNode()
        year_node.tag = current_year
        month_node = ArchiveNode()
        current_month = all_posts[i].date_added.month
        month_node.tag = current_month

        while i < len(all_posts) and current_year == all_posts[i].date_added.year:

            if all_posts[i].date_added.month != current_month:
                current_month = all_posts[i].date_added.month
                month_node = ArchiveNode()
                month_node.tag = current_month
                month_node.children = []

            while i < len(all_posts) \
                    and current_year == all_posts[i].date_added.year \
                    and current_month == all_posts[i].date_added.month:
                month_node.children.append(all_posts[i])
                i += 1

            year_node.children.append(month_node)

        archive.append(year_node)

    context = {'archive_tree': archive}
    return render(request, 'blog_app/archive.html', context)
