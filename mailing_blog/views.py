from django.shortcuts import render
from django.utils.text import slugify

from mailing_blog.forms import BlogForm
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView

from mailing_blog.models import Blog
from mailing_blog.services import get_blog_list_from_cache


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm

    success_url = reverse_lazy("mailing_blog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("mailing_blog:blog_detail", args=[self.object.pk])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return get_blog_list_from_cache()
class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("mailing_blog:blog_list")

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("mailing_blog:blog_detail", args=[self.object.pk])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("mailing_blog:blog_list")

