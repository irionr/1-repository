from __future__ import unicode_literals

from django.db import models


class Category(models.Model) :
    """
    this is the Category model
    """
    name = models.CharField( max_length=512, null=False)
    slug = models.SlugField(null=False, unique=True, max_length=255)

    def __str__(self):
        """ Returns the representation of the model, which is used in
        the Django Admin interface
        """
        return "Category : %s" % self.name
    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('category', kwargs={'slug': str(self.slug)})

class Post(models.Model) :
    """
    This model represent a post of the blog
    """
    title = models.CharField(max_length=1024, null=False)
    slug = models.SlugField(null=False, unique=True, max_length=255)
    category = models.ForeignKey('Category')
    content = models.TextField(null=False)
    date = models.DateField()
    author = models.ForeignKey('auth.User')
    is_published = models.BooleanField(null=False, default=False)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post', kwargs={'slug': str(self.slug)})

    @property
    def excerpt(self):
        return self.content[0:100] + "..."

    def __str__(self) :
        """
        Returns the string representation of the model, which i used in
        the Django Admin interface

        """
        return "Post: %s" % self.title

class Comment(models.Model):
    """
    This represents a comment to the post
    """
    content = models.TextField(null=False)

    date = models.DateField()
    author = models.ForeignKey('auth.User')
    post = models.ForeignKey('Post')


    @property
    def gravatar_url(self):
        """
        Returns the gravatar URL for this user
        """
        import hashlib
        m = hashlib.md5()
        m.update(self.author.email.encode())
        return "https://www.gravatar.com/avatar/" + m.hexdigest()

    def __str__(self):
        """
        Returns the string sapresentation of the model, wich i used in the
        Django Admin interface
        """
        return "Comment: %s" % self.content


