from haystack import indexes
from products_monitor.models import Brand, Product

"""
class BrandIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Brand

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
"""

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        return self.get_model().objects.all()