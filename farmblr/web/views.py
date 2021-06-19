from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def marketplace(request):
    return render(request, 'marketplace.html')
