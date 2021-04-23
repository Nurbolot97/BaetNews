from django.contrib import admin
from .models import (Post, Comment, 
                    PostImage)


class ImageInlineAdmin(admin.TabularInline):

    model = PostImage
    fields = ('image',)
    max_num = 3


@admin.register
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin]


admin.site.register(Comment)