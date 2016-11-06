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
    post = models.ForeignKey(Post)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        """Return a string representation of the model"""
        return self.text[:50] + "..."
