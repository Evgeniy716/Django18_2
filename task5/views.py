from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm



# def sign_up_by_html(request):
#     users = {
#         'Ivan': 'Ivan1999','Petr': 'Petya2005'
#     }
#     info = {
#     }
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         repeat_password = request.POST.get("repeat_password")
#         age = request.POST.get("age")
#
#         if password == repeat_password and int(age) >= 18 and username not in users:
#             return HttpResponse(f"Приветствуем, {username}!")
#         elif password != repeat_password:
#             info['error'] = 'Пароли не совпадают'
#         elif int(age) < 18:
#             info['error'] = 'Вы должны быть старше 18'
#         elif username in users:
#             info['error'] = 'Пользователь уже существует'
#
#     return render(request, 'fifth_task/registration_page.html', context=info)



def sign_up_by_django(request):
    users = {
        'Ivan': 'Ivan00','Petr': 'Petr11'
    }
    info = {'error': None}
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] != cd['repeat_password']:
                info['error'] = "Пароли не совпадают"
            elif cd['age'] < 18:
                info['error'] = "Вы должны быть старше 18"
            elif cd["username"] in users:
                info['error'] = "Пользователь уже существует"
            else:
                return HttpResponse(f"Приветствуем, {cd['username']}!")

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)