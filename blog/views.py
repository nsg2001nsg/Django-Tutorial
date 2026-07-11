from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Nandini',
        'title': 'Blog Post 1',
        'content': 'Content for blog 1',
        'date_posted': 'July 11, 2026'
    },
    {
        'author': 'Nandini',
        'title': 'Blog Post 2',
        'content': 'Content for blog 2',
        'date_posted': 'July 12, 2026'
    },
    {
        'author': 'Nandini',
        'title': 'Blog Post 3',
        'content': 'Content for blog 3',
        'date_posted': 'July 13, 2026'
    },
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
