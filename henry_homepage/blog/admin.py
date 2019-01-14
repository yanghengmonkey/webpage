from django.contrib import admin
from django.forms.widgets import TextInput
from django.db import models
#from markdownx.admin import MarkdownxModelAdmin
from martor.widgets import AdminMartorWidget
from martor.models import MartorField
from . models import Post
from . forms import PostCharForm

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.CharField: {'widget': TextInput(attrs={'size': '100'})},
            MartorField: {'widget': AdminMartorWidget},
            models.TextField: {'widget': AdminMartorWidget},
    }
admin.site.register(Post, PostAdmin)
