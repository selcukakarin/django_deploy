from django.contrib import admin
from django.urls import path

from .views import index, about, detail, dashboard, addArticle, updateArticle, deleteArticle, articles

app_name = "article"

# http://127.0.0.1:8000/
urlpatterns = [
    path("create/", index, name="index1"),
    path("<int:id>", detail, name="detail"),
    path("deneme1", index, name="detail1"),
    path("deneme2", index, name="detail2"),
    path("deneme3", index, name="detail3"),
    path("dashboard/", dashboard, name="dashboard"),
    path("addarticle/", addArticle, name="addarticle"),
    path("article/<int:id>", detail, name="detail"),
    path("update/<int:id>", updateArticle, name="update"),
    path("delete/<int:id>", deleteArticle, name="delete"),
    path("", articles, name="articles"),

]
