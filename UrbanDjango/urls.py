from django.contrib import admin
from django.urls import path
from task2.views import task2_func_view, ViewByClass
from task3.views import *
from task4.views import *
from task5.views import sign_up_by_html,sign_up_by_django
urlpatterns = [
    path('admin/', admin.site.urls),
    path('func_view/', task2_func_view),
    path('class_view/', ViewByClass.as_view()),
    path('platform/', game_platform),
    path('platform/games/', game),
    path('platform/cart/', cart),
    path('', sign_up_by_html),
    path('', sign_up_by_django)
]


