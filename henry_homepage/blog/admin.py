from django.contrib import admin
from django.db import models
from markdownx.admin import MarkdownxModelAdmin
from . models import Post

# Register your models here.
admin.site.register(Post)
