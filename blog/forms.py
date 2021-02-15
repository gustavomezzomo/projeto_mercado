from django import forms

from .models import Post
from .models import product


class PostForm(forms.ModelForm):

    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ('image',)

class productform(forms.ModelForm):

    image = forms.ImageField(required=False)

    class Meta:
        model = product
        fields = ('image','title')