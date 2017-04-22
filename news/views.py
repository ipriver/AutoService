from django.shortcuts import render
from django.views import generic

from news.models import Article


def test(request):
    latest_news_list = Article.objects.order_by('-date')[:5]
    context = {
        'latest_news_list': latest_news_list,
    }
    return render(request, 'news/index.html', context)


def tr(request, id_key=5, p2_key=4):
    return HttpResponse('<p>'+id_key+'</p>'+'<p>'+p2_key+'</p>')


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('-date')[:5]