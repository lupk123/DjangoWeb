from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField("标题", max_length=30)
    author = models.CharField("作者", max_length=30)
    content = models.TextField()
    date = models.DateTimeField("添加时间", auto_now_add=True)
    modifyDate = models.DateTimeField("修改时间", auto_now=True)
    label = models.CharField("标签", max_length=20)

    class Meta:
        db_table = "article"

    def __str__(self):
        return self.title