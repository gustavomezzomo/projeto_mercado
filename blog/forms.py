from django import forms

from .models import Post
from .models import Product

class PostForm(forms.ModelForm):

    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ('image',)

class ProductForm(forms.ModelForm):

    image = forms.ImageField(required=True)

    class Meta:
        model = Product
        fields = ('image',)