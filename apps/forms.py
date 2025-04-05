from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.hashers import make_password
from .models import Users, Blog


class UserCreateForm(ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'username', 'password']



    def clean_password(self):
        password = self.cleaned_data['password']
        return make_password(password)
    

class UserLoginForm(Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'title', 'day', 'image']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),
        }