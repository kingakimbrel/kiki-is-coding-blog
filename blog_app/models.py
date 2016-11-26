from django.db import models


class Post(models.Model):
    """A class representing a post."""
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        """Return a string representation of the model"""
        return self.text[:50] + "..."


class Comment(models.Model):
    """Comments related to specific post."""
    post = models.ForeignKey(Post, related_name='comments')
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        """Return a string representation of the model"""
        return self.text[:50] + "..."


class ArchiveYearNode:
    """A class representing a year node of Archive view."""

    def __init__(self):
        self.year = 0
        self.months = []


class ArchiveMonthNode:
    """A class representing a month node of Archive view."""

    def __init__(self):
        self.month = ""
        self.month_num = 0
        self.count = 0
