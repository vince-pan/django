from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")


def about_us(request):
    return HttpResponse("<h1>A propos</h1> <p>Moi c'est Vince, je suis un gros botch !</p>")


def contact_us(request):
    return HttpResponse("<h1>Nous contacter</h1> <p>contact</p>")


def listings(request):
    return HttpResponse("<h1>Listes</h1> <p>listes</p>")
