from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


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


class CreateProfile(forms.ModelForm):
    COUNTRIES = (
        ("Kenya", "Kenya"),
    )
    COUNTRY_CODES = (
        ("254", "+254"),
    )
    country_code = forms.ChoiceField(choices=COUNTRY_CODES)
    country = forms.ChoiceField(choices=COUNTRIES)
    postal_code = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": 'Postal Code'}))
    street = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={"Placeholder": 'Street'}))
    city = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={"Placeholder": 'city'}))
    profile_picture = forms.ImageField(required=False)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type": 'date'}))
    id_number = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": ' National Id/Passport Number'}))
    mobile = forms.CharField(max_length=9, widget=forms.NumberInput(attrs={"placeholder": "Phone No. Eg. 712345678"}))

    class Meta:
        model = Profile
        fields = ['gender', 'date_of_birth', 'id_number',
                  'country', 'country_code', 'mobile', 'street', 'city', 'postal_code']

    def clean(self, *args, **kwargs):
        # Confirm age > 18
        age = calculate_age(self.cleaned_data.get('date_of_birth'))
        if age < 18:
            self.errors['date_of_birth'] = self.error_class(["You are too Young!!!"])
        # check that phone number is valid
        mobile = self.cleaned_data.get('mobile')
        if not str(mobile).isdecimal():
            self.errors['mobile'] = self.error_class(['Enter only numbers (0 - 9) '])
        #  Merge country code with the mobile number
        mobile = str(self.cleaned_data.get("country_code")) + str(self.cleaned_data.get('mobile'))
        self.cleaned_data['mobile'] = mobile
        return super(CreateProfile, self).clean(*args, **kwargs)