from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)

TAGS = (
    ('Python', 'Python'),
    ('JS', 'JavaScript'),
    ('CSS', 'Cascading Style Sheet'),
    ('HTML', 'Hypertext Markup Language'),
    ('Node', 'NodeJS'),
    ('Django', 'Django Framework'),
    ('React', 'ReactJS Framework')
)

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.CharField(max_length=50, choices=TAGS)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title