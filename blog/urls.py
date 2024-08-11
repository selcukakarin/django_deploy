"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from article.views import index, about, detail
from .views import frontend, hakkimizda
from django.conf import settings
from django.conf.urls.static import static

# http://127.0.0.1:8000
# http://127.0.0.1:8000/frontend/ sa sagfasfas
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("articles/", include("article.urls")),
    path("comments/", include("comment.urls")),
    path("user/", include("user.urls")),
    path("frontend/", frontend, name="frontend"),
    path('tinymce/', include('tinymce.urls')),
    path("hakkimizda/", hakkimizda, name="hakkimizda"),
]
# http://127.0.0.1:8000/user/register

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
