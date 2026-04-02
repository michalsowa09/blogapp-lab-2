from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = "posts"
    template_name = "blog/post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
