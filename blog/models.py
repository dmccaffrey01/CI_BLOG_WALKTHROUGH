from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, default="", unique=True)
    slug = models.SlugField(max_length=200, default="", unique=True)
    author = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(default="")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    create_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-create_on']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, default="", on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80, default="", unique=True)
    email = models.EmailField(default="")
    body = models.TextField(default="")
    create_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['create_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

