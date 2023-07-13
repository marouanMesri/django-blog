from django.shortcuts import render

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from posts.models import BlogPost
from django.urls import reverse_lazy


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content', 'published']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published']

    def get_queryset(self):
        queryset = super().get_queryset()
        fields = ['title', 'content', 'published']
        return queryset.filter(author=self.request.user)


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blogpost_detail.html"


class BlogPostDelete(DeleteView):
    model = BlogPost
    template_name = "posts/blogpost_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy('posts:home')
