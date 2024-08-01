from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="заголовок")
    slug = models.CharField(max_length=100, verbose_name="slug")
    content = models.TextField(verbose_name='содержимое')
    image_preview = models.ImageField(
        upload_to="blog/image",
        verbose_name="предварительный просмотр",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=False, verbose_name="опубликованные посты")
    views_count = models.PositiveIntegerField(default=0, verbose_name="количество просмотров")

    def __str__(self):
        return f"{self.title}: {self.content}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", "slug"]
