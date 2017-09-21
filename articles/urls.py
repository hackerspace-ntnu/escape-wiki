from django.conf.urls import url, include
from .views import ArticleView

urlpatterns = [
    url(r'^(?P<article_id>[0-9]+)/', ArticleView.as_view()),
]
