from django import forms
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'status', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
