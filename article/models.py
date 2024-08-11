from django.db import models
# from ckeditor.fields import RichTextField
from tinymce import models as tinymce_models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="yazar")
    title = models.CharField(max_length=50)
    # content = RichTextField()
    content = tinymce_models.HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank=True, null=True, verbose_name="Makaleye fotoğraf ekleyin")

    def __str__(self):
        return self.title
