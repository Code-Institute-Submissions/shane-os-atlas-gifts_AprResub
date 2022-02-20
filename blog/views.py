""" Blog Posts Views"""
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post
from blog.forms import BlogForm


def blog_show(request):
    """ Sow All Blog Posts """
    posts = Post.objects.all().order_by('posted_date')

    context = {
        "posts": posts,
    }

    return render(request, "blog/blog.html", context)


@login_required
def create_post(request):
    """ Create Blog Post """
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog')
    else:
        form = BlogForm()

    context = {
        "form": form
    }

    return render(request, 'blog/blog_post_create.html', context)


@login_required
def edit_blog(request, blog_id):
    """ Edit Blog Post """
    post = get_object_or_404(Post, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog successfully updated!")
            return redirect(reverse('blog'))
        else:
            messages.error(request, "Error: Blog update was unsuccessful! Please check the form and try again.")
    form = BlogForm(instance=post)

    template = 'blog/blog_post_edit.html'
    context = {
        'form': form,
        'post': post
    }
    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete Blog Post """
    post = get_object_or_404(Post, pk=blog_id)
    post.delete()
    messages.success(request, "Blog post successfully deleted!")
    return redirect(reverse('blog'))
