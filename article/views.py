from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from article.forms import ArticleForm
from article.models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context = {
        "numbers": ["elma", "armut", "kivi"]
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    context = {
        "article": article,
        "comments": comments
    }
    return render(request, "detail.html", context)


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla oluşturuldu.")
        return redirect("article:dashboard")
    context = {
        "form": form
    }
    return render(request, "addArticle.html", context)


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarıyla güncellendi.")
        return redirect("article:dashboard")
    context = {
        "form": form
    }
    return render(request, "update.html", context)


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()

    messages.success(request, "Makale başarıyla silindi.")
    return redirect("article:dashboard")


def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(Q(title__contains=keyword) | Q(content__contains=keyword))
    else:
        articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


