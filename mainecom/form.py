from django import forms
from .models import Books,User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'box','placeholder':'Enter username'}))
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'box','placeholder':'Enter first name'}))    
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'box','placeholder':'enter the email'}))
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'box','placeholder' : 'Enter password'}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'box','placeholder': 'Confirm password'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'email', 'password1', 'password2']




class bookform(forms.ModelForm):
    book_title = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Book Name'}))
    author = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Author\'s Name'}))
    description = forms.CharField(label='',widget=forms.Textarea(attrs={'class': 'box', 'placeholder': 'Enter Description'}))
    image = forms.ImageField(label='Add image',widget=forms.ClearableFileInput(attrs={'class': 'box', 'placeholder': 'Add Image'}))
    prize = forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class': 'box', 'placeholder': 'Enter Prize'}))

    class Meta:
        model = Books  # Use your actual model for books
        fields = ['book_title', 'author', 'description', 'image', 'prize']

    