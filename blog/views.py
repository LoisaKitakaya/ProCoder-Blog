from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.

# home/index.html view
def home(request):

    posts = Article.objects.filter(status=1).order_by('-created_on')

    context = {
        'posts' : posts
    }

    return render(request, 'blog/index.html', context)

# blog post/article.html view
class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'blog/article.html'
