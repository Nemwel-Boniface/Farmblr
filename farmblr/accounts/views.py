import json
import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

from .forms import LoginForm, CreateUser, CreateProfile
from .models import Profile, Cart

from ..products.models import Product


# Create your views here.
def login_(request):
    if request.user.is_authenticated:
        return redirect('/marketplace/')
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


@login_required
def logout(request):
    django_logout(request)
    return redirect('/')


def sign_up(request):
    sign_up_ = CreateUser(request.POST or None)
    if sign_up_.is_valid():
        username = sign_up_.cleaned_data.get('username')
        password = sign_up_.cleaned_data.get('password')
        sign_up_.save()
        authenticate(username=username, password=password)
        user = User.objects.get(username=username)
        login(request, user)
        # TODO: User email confirmation
        # sendConfirm(user)
        # return redirect(activate)
    context = {
        "sign_up": sign_up_,
    }
    return render(request, 'accounts/signup.html', context)


def validateUsername(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        pattern = re.compile('[^a-zA-Z0-9@\+.\-_]+')
        if bool(re.search(pattern, username)):
            return JsonResponse({'username_error': "Only alphanumeric characters, @, ., +, -,  _ allowed"}, status=400)
        if len(username) > 150:
            return JsonResponse({'username_error': "Username should be 150 characters or fewer in length"})
        if User.objects.filter(username=username).exists():
            return JsonResponse({"username_error": "Sorry, that username is taken"}, status=409)
        return JsonResponse({"username_valid": True})


def validateMobile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_number = data['mobile']
        if len(phone_number) > 9:
            return JsonResponse({'mobile_error': "Enter a valid phone Number (9 digits)"})
        return JsonResponse({"mobile_valid": True})


def validateEmail(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data['email']
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': "Email Already in Use"}, status=409)
        return JsonResponse({"email_valid": True})


def validatePassword(request):
    if request.method == "POST":
        data = json.loads(request.body)
        password1 = data['password1']
        password2 = data['password2']
        if str(password1) != str(password2):
            return JsonResponse({'password_error': "The two passwords don't match"})
        return JsonResponse({"password_match": True})


@login_required
def profile(request, username):
    profile_ = CreateProfile(request.POST or None)
    user = User.objects.get(username=username)
    if request.user != user:
        return redirect(login_)
    if profile_.is_valid():
        gender = profile_.cleaned_data.get('gender')
        date_of_birth = profile_.cleaned_data.get('date_of_birth')
        id_number = profile_.cleaned_data.get('id_number')
        mobile = profile_.cleaned_data.get('mobile')
        country = profile_.cleaned_data.get('country')
        street = profile_.cleaned_data.get('street')
        city = profile_.cleaned_data.get('city')
        postal_code = profile_.cleaned_data.get('postal_code')
        profile_picture = request.FILES.get('profile_picture')

        profile_ = Profile.objects.create(user=user, id_number=id_number, country=country, street=street,
                                          date_of_birth=date_of_birth, gender=gender, mobile=mobile,
                                          city=city, postal_code=postal_code, profile_picture=profile_picture)
        profile_.save()
        return redirect('/marketplace/')
    context = {
        "profile": profile_,
    }
    return render(request, 'accounts/profile.html', context)


def add_to_cart(request, id):
    if not request.user.is_authenticated:
        return redirect(login_)
    product = Product.objects.get(id=id)
    new_product = Cart.objects.create(product=product, user=request.user)
    new_product.save()
    return redirect('products')


@login_required
def delete_cart(request, id):
    Cart.objects.get(product=id).delete()
    return redirect('products')
