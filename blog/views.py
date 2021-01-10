from django.shortcuts import render
from blog.models import Post, Comment
from django.views.generic import (TemplateView, ListView)#parenthesis to extend to multiple lines

class AboutView(TemplateView):
    #TODO na brw ti einai kai apo pou erxetai to template_name
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # This line utilizes Django ORM to translate that to a SQl query on the models
        # 
        # Grab the *Post* model
        # *All the objects* from there
        # *Filter out* based on the conditions in the parenthesis 
        #
        # Grab the published_date (__lte == less than or equal to) the current time https://docs.djangoproject.com/en/3.1/ref/models/querysets/
        # Then order them by published date
        # The underscore before the -published_date in order_by specifies if the ordering will be ascending or descending.
        # In this case descending
        return Post.objects.filter(published_date__lte=timezone.now(), order_by('-published_date'))