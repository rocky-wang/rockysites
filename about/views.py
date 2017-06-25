# coding: utf-8
import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Todo


# Create your views here.
def old_add(request):
    a1 = request.GET.get('a', 0)
    a2 = request.GET.get('b', 0)
    result = int(a1) + int(a2)
    return HttpResponse('the result is %d' % result)


def add(request):
    a1 = request.GET.get('a', 0)
    a2 = request.GET.get('b', 0)
    logging.debug(reverse('calc_add', args=(10, 20)))
    # result = int(a1) + int(a2)
    # return HttpResponse('the result is %d' % result)
    return HttpResponseRedirect(reverse('calc_add', args=(a1, a2)))


def new_add(request, a1, a2):
    result = int(a1) + int(a2)
    return HttpResponse('New result is %s' % result)


def about_index(request):
    art1 = '热门电影'
    movies = map(str, xrange(100))
    content_data = {'title': art1, 'mvs': movies}
    return render(request, 'about/index.html', context=content_data)


def about_todo(request):
    datas = Todo.objects.all()[:10]

    content = {'todos': datas}

    return render(request, 'about/todos.html', context=content)


def about_detail(request, n):
    datas = Todo.objects.get(id=n)

    content = {'todos': datas}

    return render(request, 'about/detail.html', context=content)
