from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32,default='Title') #第一个参数是必须的，定义长度
    content = models.TextField(null=True)#TextField()所有参数都是非必须的
    def __str__(self):
        return self.title