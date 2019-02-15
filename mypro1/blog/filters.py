from django.contrib.auth.models import User
import django_filters
from .models import Post

class BlogFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['author', 'title',]