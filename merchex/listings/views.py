from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def about_us(request):
    return HttpResponse("<h1>A propos</h1> <p>Moi c'est Vince, je suis un gros botch !</p>")


def contact_us(request):
    return HttpResponse("<h1>Nous contacter</h1> <p>contact</p>")


def listings(request):
    return HttpResponse("<h1>Listes</h1> <p>listes</p>")
