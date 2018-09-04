from .models import Column,Article


def nav_column(request):
    nav_display_columns = Column.objects.filter(nav_display=True)
    home_display_columns = Column.objects.filter(home_display=True)
    new_articles = Article.objects.all().order_by('-pub_date')[:10]

    news_history = request.COOKIES.get('news_history')
    news_history_lsit = []

    if news_history:
        news_pk_lsit = news_history.split(',')
        # 倒序加入另一个列表，使得最近一次的浏览能被第一个遍历
        for each_new in range(len(news_pk_lsit)-1,-1,-1):
            each_new = Article.objects.get(pk=int(news_pk_lsit[each_new]))
            news_history_lsit.append(each_new)
    context = {
        'nav_display_columns': nav_display_columns,
        'home_display_columns': home_display_columns,
        'new_articles':new_articles,
        'news_history_lsit':news_history_lsit
    }

    return context