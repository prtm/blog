# stdlib

# core django
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# project related
from .models import Post


# Create your views here.


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 8)  # 8 posts in each page

    offset = request.GET.get('offset')
    if offset is None or offset == '':
        page = 1
    else:
        try:
            page = int(request.GET.get('offset'))//8
        except Exception:
            page = 1
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver the last page
        posts = paginator.page(paginator.num_pages)
    print(posts)
    return render(request,
                  'blog/home.html',
                  {'page': page,
                   'posts': posts,
                   'paginator': paginator
                   })
