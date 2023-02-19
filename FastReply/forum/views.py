from django.shortcuts import render


def home(request):
    return render(request, 'forum/Home.html')


def questions(request):
    return render(request, 'forum/Questions.html')


def devs(request):
    return render(request, 'forum/Devs.html')


def reg(request):
    return render(request, 'forum/Reg.html')


def login(request):
    return render(request, 'forum/Login.html')
