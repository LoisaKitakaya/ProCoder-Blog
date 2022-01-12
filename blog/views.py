from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):

    posts = Article.objects.filter(status=1).order_by('-created_on')

    context = {
        'posts' : posts
    }

    return render(request, 'blog/index.html', context)
