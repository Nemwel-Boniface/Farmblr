from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post
from .forms import CommentForm


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


def blogPost(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)
    comments = blog_post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = blog_post
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'post': blog_post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'blog/post.html', context)
