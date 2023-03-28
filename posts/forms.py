from django import forms

from posts.models import Post, Comment


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("description", "image")
        labels = {
            'image': 'Фото',
            'description': 'Текст',
        }


class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ("text",)
        labels = {
            'text': 'Комментапий'
        }
