from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request,"blog/index.html")

def posts(request):
    return None

def posts_detail(request):
    return None