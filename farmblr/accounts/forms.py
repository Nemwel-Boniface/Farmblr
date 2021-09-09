from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = User.objects.filter(username=username)
        if not user:
            raise forms.ValidationError("This user does not exist")
        elif username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User is not Active")

        return super(LoginForm, self).clean(*args, **kwargs)


class CreateUser(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'email@example.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        users = User.objects.all()
        email_qs = users.filter(email=email)
        if email_qs:
            self.errors['email'] = self.error_class(["This email is already registered"])
        return super(CreateUser, self).clean(*args, **kwargs)