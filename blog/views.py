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


# news/news.html view
def news(request):

    from newsapi import NewsApiClient

    # Init
    newsapi = NewsApiClient(api_key='664f61cf91624b3098f8825a6282e25e')

    # /v2/top-headlines
    news_feed = newsapi.get_everything(q='software', sources='the-verge,bbc-news,ars-technica,bloomberg,business-insider', language='en', sort_by='relevancy')

    print(news_feed)

    context = {
        'news_feed' : news_feed['articles']
    }

    return render(request, 'blog/news.html', context)