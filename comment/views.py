from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from article.models import Article
from comment.models import Comment


# Create your views here.

def addComment(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author=comment_author, comment_content=comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:detail", kwargs={"id": article_id}))
