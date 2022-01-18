from django.views import generic

from .models import Post


class PostIndex(generic.ListView):
    model = Post
