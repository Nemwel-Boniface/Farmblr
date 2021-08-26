from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm


# Create your views here.
def login_(request):
    if request.user.is_authenticated:
        pass
        # TODO Redirect to Dashboard
    next_ = request.GET.get('next')
    # login form
    log_in = LoginForm(request.POST or None)
    if log_in.is_valid():
        username = log_in.cleaned_data.get('username')
        password = log_in.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next_:
            redirect(next_)
        return redirect('dashboard')
    context = {
        'log_in': log_in,
    }
    return render(request, 'accounts/login.html', context)