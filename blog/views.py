from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Setor, Product
from .forms import PostForm
from django.shortcuts import redirect
import logging
import json
from django.http import JsonResponse

logger = logging.getLogger(__name__)


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):

    if request.method == "POST":
         form = PostForm(request.POST, request.FILES)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
    else:
         form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
         form = PostForm(request.POST, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
    else:
         form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'pk': pk})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def image(request):
    post = Post.objects.order_by('-published_date').first()
    return JsonResponse(post.to_json_dict())

def setor_detail(request, slug):
    setor = get_object_or_404(Setor, slug=slug)
    products = Product.objects.filter(setor=setor)
    return JsonResponse({'slug':slug, 'setor':setor.to_dict_json(), 'products':[p.to_dict_json() for p in products]})