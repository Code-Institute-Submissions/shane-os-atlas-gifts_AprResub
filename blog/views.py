from django.shortcuts import render
from blog.models import Post

def blog_id(request):
    posts = Post.objects.all().order_by('posted_date')
    context = {
        "posts": posts,
    }
    return render(request, "blog.html", context)
