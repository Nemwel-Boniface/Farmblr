from django.shortcuts import render
from .models import Product, Category


# Create your views here.
def marketplace(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'products/marketplace.html', context)
