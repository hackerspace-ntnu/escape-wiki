from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from articles.models import Article


class Index(View):
    def get(self, request, *args, **kwargs):
        try:
            context = {
                'article': Article.objects.get(code=kwargs['url'])
            }
            return render(request, 'articles/article.html', context)
        except Article.DoesNotExist:
            return HttpResponseRedirect('/101')

        #return render(request, 'wiki/index.html')


    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect('/%s' % request.POST.get('code'))
