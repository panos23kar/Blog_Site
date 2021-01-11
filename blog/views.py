from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView) #parenthesis to extend to multiple lines

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
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    # In order to create a Post you have to be loggedin

    # Attr from LoginRequiredMixin: redirects you if you are not loggedin
    login_url = '/login/'
    # Attr from LoginRequiredMixin: redirects after you create a Post
    redirect_field_name = 'blog/post_detail.html'
    
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # Waits till the instance/object is deleted and then redirects the user to the success_url
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


##############################################################################################
#####################################-----Comment----#########################################

#Decorator which allows only logged in users to access this view
@login_required
def add_comment_to_post(request, pk):
    # pk = primary key of the post to which the comment refers
    # get_object_or_404 tries to get the corresponding model otherwise 404 page
    post = get_object_or_404(Post, pk=pk)
    
    # When the user has filled in the CommentForm (we have imported it from blog.forms)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # If form is valid bult-in Django
        if form.is_valid():
            # Dont save it in the database yet due to commit=False
            comment = form.save(commit=False)
            # Connect the foreign key of comment model with the corresponding Post
            comment.post = post
            # Save into the database
            comment.save()
            # After saving in the databse, redirect to the post_detail view
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})
