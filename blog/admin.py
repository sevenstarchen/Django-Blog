from django.contrib import admin
from . import models
from .models import Article #models前面加点表明当前目录
# Register your models here.
admin.site.register(Article)