from django.contrib import admin

from articles.models import Article, Hint

admin.site.register(Article)
admin.site.register(Hint)
