from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post


# Create your views here.
def blog(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:    # if page is not an integer, deliver 1st page
        posts = paginator.page(1)
    except EmptyPage:  # if page is out of range, deliver last page of results
        posts = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page)
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'blog/blogs.html', context)
