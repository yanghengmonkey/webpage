from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse
from tinymce.models import HTMLField
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.
class Post(models.Model):
    title = models.CharField( max_length=200)
    author = models.CharField(max_length=50, default='Henry Yang')
    created_date = models.DateTimeField( default= timezone.now )
    published_date = models.DateTimeField( default= timezone.now )
    #content = HTMLField( )
    content = MarkdownxField()
    post_logo = models.FileField(max_length=100, default='', blank=True)
    tags = TaggableManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def formatted_markdown(self):  # <--- We'll need this for views.py later
        return markdownify(self.content)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs  = {'pk':self.pk} )
