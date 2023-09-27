from django.shortcuts import render

# Create your views here.
# posts/views.py

from django.http import HttpResponse
from .data import POSTS

def all_posts(request):
    # Create a plain text representation of all blog posts
    all_posts_text = "\n".join([f"Title: {post['title']}\nContent: {post['content']}\n" for post in POSTS])
    
    # Return the plain text as an HttpResponse
    return HttpResponse(all_posts_text, content_type='text/plain')
