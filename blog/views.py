from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .models import product
from .forms import productform
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

def product_edit(request, pk):
    product = get_object_or_404(product, pk=pk)
    if request.method == "product":
         form = ProductForm(request.product, instance=product)
    if form.is_valid():
        product = form.save(commit=False)
        product.author = request.user
        product.published_date = timezone.now()
        product.save()
        return redirect('product_detail', pk=product.pk)
    else:
         form = productForm(instance=product)
    return render(request, 'blog/product_edit.html', {'form': form, 'pk': pk})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')


def image(request):
    product = Product.objects.order_by('published_date')
    return JsonResponse(product.to_json_dict())

def product_list(request):
    product = Product.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/product_list.html', {'product': product})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'blog/product_detail.html', {'product': product})


def product_new(request):

    if request.method == "product":
         form = productForm(request.product, request.FILES)
         if form.is_valid():
             product = form.save(commit=False)
             product.author = request.user
             product.published_date = timezone.now()
             product.save()
             return redirect('product_detail', pk=product.pk)
    else:
         form = productForm()
    return render(request, 'blog/product_edit.html', {'form': form})


