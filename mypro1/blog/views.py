from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post
from .filters import BlogFilter
def post_list_view(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


		
def search(request):
    blog_list = Post.objects.all()
    blog_filter = BlogFilter(request.GET, queryset=blog_list)
    return render(request, 'blog/post/search.html', {'filter': blog_filter})

