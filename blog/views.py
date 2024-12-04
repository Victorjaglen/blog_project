from django.shortcuts import render
from .models import Blog


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def blogs(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blogs.html', {'blogs': blogs})


def blog_page(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog_page.html', {'blog': blog})
