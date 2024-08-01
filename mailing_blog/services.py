from django.core.cache import cache

from mailing_blog.models import Blog
from config.settings import CACHE_ENABLED


def get_blog_list_from_cache():
    blog_list = Blog.objects.all()
    if not CACHE_ENABLED:
        return blog_list
    key = 'blog_list'
    blog = cache.get(key)
    if blog is None:
        cache.set(key, blog_list)
        return blog_list
    return blog
