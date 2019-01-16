import datetime
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    #content = indexes.MartorField(model_attr='content')
    #tags = TaggableManager()
    published_date = indexes.DateTimeField(model_attr='published_date')



    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(published_date__lte=datetime.datetime.now())
