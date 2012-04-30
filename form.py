from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        widgets = {
            'thread': HiddenInput(),
        }