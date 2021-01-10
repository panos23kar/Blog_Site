from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post

        # specify the fields that I can edit via the form
        fields = ('author', 'title', 'text')

        #Connect widgets to css attributes
        # This is to grab a particular fields widget so as to assign css classes to it/them
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }