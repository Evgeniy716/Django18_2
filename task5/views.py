from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm



def sign_up_by_html(request):
    users = {
        'Ivan': 'Ivan1999','Petr': 'Petya2005'
    }
    info = {
    }
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        if password == repeat_password and int(age) >= 18 and username not in users:
            return HttpResponse(f"Приветствуем, {username}!")
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'

    return render(request, 'fifth_task/registration_page.html', context=info)

def sign_up_by_django(request):
    users = {
        'Ivan2': 'Ivan1999','Petr2': 'Petya2005'
    }
    info = {
    }
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data("username")
            password = form.cleaned_data("password")
            repeat_password = form.cleaned_data("repeat_password")
            age = form.cleaned_data("age")

            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f"Приветствуем, {username}!")
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
        else:
            form = ContactForm()

        return render(request, 'fifth_task/registration_page.html', {'form': form})