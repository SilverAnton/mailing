from django.contrib import admin

from mailing_blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "content",
    )
    search_fields = (
        "title",
        "slug",
        "content",
    )
