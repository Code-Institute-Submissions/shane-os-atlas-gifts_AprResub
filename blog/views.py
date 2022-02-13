""" Blog Posts Views"""
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from blog.forms import BlogForm


def blog_show(request):
    """ Sow All Blog Posts """
    posts = Post.objects.all().order_by('posted_date')

    context = {
        "posts": posts,
    }

    return render(request, "blog.html", context)


def create_post(request):
    """ Create Blog Post """
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog_show')
    else:
        form = BlogForm()

    context = {
        "form": form
    }

    return render(request, 'blog_post_create.html', context)


def edit_blog(request, blog_id):
    """ Edit Blog Post """
    blog_post = get_object_or_404(Post, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = BlogForm(instance=blog_post)
    context = {
        'form': form
    }
    return render(request, 'blog/edit_blog.html', context)
