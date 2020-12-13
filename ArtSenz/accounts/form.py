from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import model_user_article

class form_user(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name','last_name','email','password')
        widgets = {
        'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.TextInput(attrs={'class':'form-control'}),
        'password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
class form_user_article(forms.ModelForm):
    class Meta():
        model = model_user_article
        fields = ('header','content')
        widgets = {
        'header' : forms.TextInput(attrs={'class':'form-control'}),
        'content' : forms.Textarea(attrs={'class':'form-control'}),
        }
