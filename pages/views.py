from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'all_post_list'


class AboutPageView(ListView):
    template_name = 'pages/about.html'