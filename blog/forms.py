from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email', 'body')

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
        )
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': "form-control",
                }
            ),
            'content': forms.TextInput(
                attrs = {
                    'class': "form-control",
                }
            )
        }



