from django.contrib import admin
from .models import Post
from .models import Setor
from .models import Product

admin.site.register(Post)
admin.site.register(Setor)
admin.site.register(Product)