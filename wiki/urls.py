from django.conf.urls import url
from django.contrib import admin
from .views import Index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'(?P<url>.*)', Index.as_view()),
]
