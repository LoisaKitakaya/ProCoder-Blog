from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from .views import *

# mapping app urls
urlpatterns = [
    path('', home, name='home'),
]