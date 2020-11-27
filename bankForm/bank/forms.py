from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20)
    surname = forms.CharField(min_length=2, max_length=30)
    patronymic = forms.CharField(min_length=2, max_length=25)
    email = forms.CharField(min_length=2, max_length=30)
    address = forms.CharField(min_length=2, max_length=100)
    phone = forms.CharField(max_length=12)

