""" Blog Posts Views"""
from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import BlogForm


def blog_id(request):
    posts = Post.objects.all().order_by('posted_date')
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog')
    else:
        form = BlogForm()

    context = {
        "posts": posts,
        "form": form
    }

    return render(request, "blog.html", context)


def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogForm()

    context = {
        "form": form
    }

    return render(request, 'blog.html', context)
