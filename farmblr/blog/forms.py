from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'email@example.com'}))
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Your Comment", }
        ),
    )

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')