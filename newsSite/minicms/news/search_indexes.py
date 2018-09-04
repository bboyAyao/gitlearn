from haystack import indexes
from news.models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    # 索引字段 use_template=True 指定根据表中的哪些字段建立索引文件的说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()