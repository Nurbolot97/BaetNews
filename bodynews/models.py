from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=200, verbose_name="Наименование")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name="Автор")
    body = models.TextField(verbose_name="Тело поста")
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="Время публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    slug = models.SlugField(max_length=255, unique_for_date='pub_date')


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta():
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"{self.title}{self.slug} - {self.author} on {self.pub_date}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name="Тело комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"Comments by {self.author} on {self.post}"


class PostImage(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='posts', verbose_name="Картинки новостей")




