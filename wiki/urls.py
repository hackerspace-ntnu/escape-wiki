from django.conf.urls import url, include
from django.contrib import admin
from .views import Index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/', include('articles.urls')),
    url(r'^$', Index.as_view()),
]
