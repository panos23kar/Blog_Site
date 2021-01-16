from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author          = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title           = models.CharField(max_length=200)
    text            = models.TextField()
    create_date     = models.DateTimeField(default=timezone.now())
    published_date  = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    # The name of this method is a django reserved name. It should be used like that
    # whenever we wabt to redirect the user somewhere after creating/deleting an instance
    # of a model
    # post_detail refers to the view that shows the details of a post
    # kwargs={'pk':self.pk}: matches the primary key with the primary key of this instance
    #     It is used by the url to redirect to the correct post detail view
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post                = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author              = models.CharField(max_length=200)
    text                = models.TextField()
    create_date         = models.DateTimeField(default=timezone.now())
    approved_comment    = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def get_absolute_url(self):
        return reverse("post_list")
    
    def __str__(self):
        return self.text