from django.forms import CharField, ModelForm, Textarea, TextInput

from .models import Post
from .validators import tags_validator


class CreatePostForm(ModelForm):
    tags = CharField(
        widget=TextInput(
            attrs={'class': 'form-control', 'id': 'tags'},
        ),
        validators=[tags_validator],
    )

    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
