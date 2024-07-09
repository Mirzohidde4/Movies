from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_post', args=[self.slug])


class Posts(models.Model):
    title = models.CharField(max_length=150,)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150)
    description = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    photo = models.ImageField(upload_to="images/%Y/%m/%d/")
    video = models.FileField(upload_to="videos/%Y/%m/%d/")
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    

class Comments(models.Model):
    post = models.ForeignKey(to=Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=50)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True    )

    def __str__(self):
        return self.comment
    
    # def get_absolute_url(self):
    #     return reverse('posts')