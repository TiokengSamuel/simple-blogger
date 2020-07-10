from django.shortcuts import render, get_object_or_404
form .models import Post

def post_list(request):
    posts = Post.published

# Create your views here.
