from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models


def index(request):  # 参数名不做要求，默认为request
    # return HttpResponse("hello world!")
    # rendenr 前两个参数是必须的
    # return render(request,'index.html',{'hello':'Hello,Blog!'})
    # article = models.Article.objects.get(pk=1)#pk=1是指主键为1
    articles = models.Article.objects.all()  # 获取所有数据
    return render(request, 'index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'index.html', {'articles': articles})

    article=models.Article.objects.get(pk=article_id)
    article.title=title
    article.content=content
    article.save()
    return render(request, 'article_page.html', {'article': article})