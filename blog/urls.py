"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('/article/(?P<article_id>[0-9]+)/', views.article_page),#使用正则表达式匹配的数字以article_id作为组名去匹配 python3不支持该写法
    path('article/<int:article_id>/', views.article_page, name='article_page'),
    path('edit/', views.edit_page,name='edit_page'),
    path('edit/action', views.edit_action,name='edit_action'),
]
app_name = 'blog'
