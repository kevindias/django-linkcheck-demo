from django.forms import ModelForm

from linkshare import models


class PostForm(ModelForm):
    """A form for Post instances."""
    class Meta:
        model = models.Post
