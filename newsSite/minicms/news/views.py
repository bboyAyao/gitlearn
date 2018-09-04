from django.shortcuts import render,redirect
from news.models import *
from django.views.generic.base import View

class IndexView(View):
    def get(self,request):
        # home_display_columns = Column.objects.filter(home_display=True)
        # nav_display_columns = Column.objects.filter(nav_display=True)
        # 首页最近更新新闻展示
        articles = Article.objects.all().order_by('-update_time')[:20]

        return render(request, 'index.html',{
            # 'home_display_columns': home_display_columns,
            # 'nav_display_columns': nav_display_columns,
            'articles':articles
        })

def column_detail(request,column_slug):
    column = Column.objects.get(slug=column_slug)
    col_art = column.article_set.all().order_by('-update_time')
    return render(request,'news/column.html', {'column': column,'col_art':col_art})


def article_detail(request,pk,article_slug):
    article = Article.objects.get(pk=pk)
    all_column = ''
    art_col = article.column.all()
    for each in art_col:
        all_column += ','+ each.name

    article.column2 = all_column
    print(all_column)
    response = render(request, 'news/article.html', {'article': article, 'art_col': art_col[0]})

    # 利用cookie记录浏览记录
    news_history = request.COOKIES.get('news_history')
    if news_history:
        news_pk_lsit = news_history.split(',')
        if len(news_pk_lsit)<5:
            if str(pk) not in news_pk_lsit:
                news_pk_lsit.append(str(pk))
                pk = ",".join(news_pk_lsit)
            else:
                news_pk_lsit.remove(str(pk))
                news_pk_lsit.append(str(pk))
                pk = ",".join(news_pk_lsit)
        else:
            if str(pk) not in news_pk_lsit:
                news_pk_lsit.pop(0)
                news_pk_lsit.append(str(pk))
                pk = ",".join(news_pk_lsit)
            else:
                news_pk_lsit.remove(str(pk))
                news_pk_lsit.append(str(pk))
                pk = ",".join(news_pk_lsit)
    response.set_cookie('news_history', pk)

    #网址更新，重定向新网址
    if article_slug != article.slug:
        return redirect(article, permanent=True)
    return response


