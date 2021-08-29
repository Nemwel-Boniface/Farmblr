from django.shortcuts import render


# Create your views here.
def marketplace(request):
    return render(request, 'products/marketplace.html')
