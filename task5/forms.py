from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label="Введите Login")
    password = forms.CharField(min_length=8, label="Введите пароль")
    repeat_password = forms.CharField(min_length=8, label="Повторите пароль")
    age = forms.IntegerField(label="Введите свой возраст")