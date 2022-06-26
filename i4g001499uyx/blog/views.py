from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from blog.models import  Post
from django.views.generic import ListView,CreateView ,DetailView, UpdateView, DeleteView


class PostListView(ListView):
    pass

class PostCreateView(CreateView):
    model = Post
    fields = '__all_'
    success_url = reverse_lazy('blog:all')

class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all_'
    success_url = reverse_lazy('blog:all')

class PostDeleteView(DeleteView):
    model = Post
    fields = '__all_'
    success_url = reverse_lazy('blog:all')

