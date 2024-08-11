from django.contrib import admin
from django.urls import path

from .views import addComment

app_name = "comment"

# http://127.0.0.1:8000/comments/comment/2
urlpatterns = [
    path('comment/<int:article_id>', addComment, name="addComment"),
]