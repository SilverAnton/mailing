from django.urls import path
from django.views.decorators.cache import cache_page
from mailing_blog.apps import MailingBlogConfig
from mailing_blog.views import BlogCreateView, BlogDeleteView, BlogUpdateView, BlogDetailView, BlogListView

app_name = MailingBlogConfig.name
urlpatterns = [
    path("mailing_blog/", BlogCreateView.as_view(), name="blog_create"),
    path("blog_list/mailing_blog/", BlogListView.as_view(), name="blog_list"),
    path("blog_detail/mailing_blog/<int:pk>/", cache_page(60)(BlogDetailView.as_view()), name="blog_detail"),
    path("edit/mailing_blog/<int:pk>/", BlogUpdateView.as_view(), name="blog_edit"),
    path("delete/mailing_blog/<int:pk>/",BlogDeleteView.as_view(), name="blog_delete"),

]
