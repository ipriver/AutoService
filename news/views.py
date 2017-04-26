from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, Http404
from news.models import Article, PriceList, About_Comment

from .forms import CommentForm


def get_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/about/')
    else:
        form = CommentForm()
    return render(request, 'about.html', {'form': form})


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        return Article.objects.order_by('-date')[:5]


class ContactsView(generic.ListView):
    template_name = 'news/contacts.html'

    def get_queryset(self):
        pass


def about(request, comment_page=1):
    comment_page = int(comment_page) - 1
    comments_per_page = 5
    comments_list = About_Comment.objects.order_by('-date')[
        comment_page * comments_per_page:comments_per_page +
        comment_page * comments_per_page]
    pages_count = len(About_Comment.objects.all()) / comments_per_page
    import math
    pages_count = math.ceil(pages_count)
    if comment_page + 1 > pages_count:
        raise Http404("Неверное значение страницы комментариев")
    form = CommentForm(request.POST)
    context = {
        'comments_list': comments_list,
        'form': form,
        'pages_count': [x for x in range(1, pages_count+1)]
    }
    return render(request, 'news/about.html', context)


def get_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = About_Comment()
            obj.author = form.cleaned_data['author']
            obj.title = form.cleaned_data['title']
            obj.comment = form.cleaned_data['comment']
            obj.save()
            
    return HttpResponseRedirect('/about/')
"""
class AboutView(generic.ListView):
    template_name = 'news/about.html'
    context_object_name = 'comments_list'

    def get_queryset(self):
        return About_Comment.objects.order_by('-date')[0:5]



    def get_comment(request):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('/about/')
        else:
            form = CommentForm()
        return render(request, 'about.html', {'form': form})
"""


class PriceListView(generic.ListView):
    template_name = 'news/pricelist.html'
    context_object_name = 'price_list'

    def get_queryset(self):
        return PriceList.objects.order_by('price')


