from django.forms import CharField, ModelForm, Textarea, TextInput

from .models import Post


class CreatePostForm(ModelForm):
    tags = CharField(
        widget=TextInput(attrs={'class': 'form-control', 'id': 'tags'})
    )

    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
