from django.shortcuts import render
# from datetime import date
from .models import Post
from django.shortcuts import get_object_or_404

def get_date(post):
    return post['date']

def starting_page(request):
    latest_posts=Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{"posts":latest_posts})



def posts(request):
    all_posts=Post.objects.all().order_by("-date")
    return render(request,"blog/all-posts.html",
    {
        "all_posts":all_posts
    })

def posts_detail(request,slug):
    identified_post= get_object_or_404(Post,slug=slug)
    return render(request,"blog/post-detail.html",
    {
        "post": identified_post 
    }) 