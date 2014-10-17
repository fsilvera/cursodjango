from django.shortcuts import render
from post.models import Post

# Create your views here.


def list_posts(request):
	posts = Post.objects.all()
	return render(request, "list_posts.html", {"posts": posts})
