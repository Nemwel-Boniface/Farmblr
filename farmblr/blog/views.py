from django.shortcuts import render


# Create your views here.
def blog(request):
    context = {

    }
    return render(request, 'blog/blogs.html', context)
