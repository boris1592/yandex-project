from django.forms import ModelForm, Textarea, TextInput

from .models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(
                attrs={'class': 'form-control'}
            ),
            'text': Textarea(
                attrs={'class': 'form-control', 'rows': '3'}
            )
        }
