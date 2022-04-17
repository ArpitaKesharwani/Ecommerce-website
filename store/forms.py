from django import forms



class LoginForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()