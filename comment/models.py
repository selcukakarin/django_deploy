from django.db import models

from article.models import Article


# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content + ' ' + str(self.comment_date)

    class Meta:
        ordering = ['-comment_date']

