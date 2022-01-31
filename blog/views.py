from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import *
import os

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


# news/news.html view
def news(request):

    from newsapi import NewsApiClient

    # Init
    newsapi = NewsApiClient(api_key=os.getenv('api_key'))

    # /v2/top-headlines
    news_feed = newsapi.get_everything(q='software', sources='the-verge,bbc-news,ars-technica,bloomberg,business-insider', language='en', sort_by='relevancy')

    context = {
        'news_feed' : news_feed['articles']
    }

    return render(request, 'blog/news.html', context)