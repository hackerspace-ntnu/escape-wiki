from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from articles.models import Article


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'wiki/index.html')


    def post(self, request, *args, **kwargs):
        try:
            code = request.POST.get('code')
            article = Article.objects.get(code=code)
            return HttpResponseRedirect('/article/%r/' % article.id)
        except Article.DoesNotExist:
            return render(request, 'wiki/index.html')
