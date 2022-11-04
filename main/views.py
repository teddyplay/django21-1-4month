from django.shortcuts import render, get_object_or_404
import datetime
from . import models
def abous_us(request):
    return render(request, 'about_us.html')


def date_now(request):
    a = datetime.datetime.now()
    return render(request, 'date_now.html', {'a':a})


def film_show(request):
    film = models.Film.objects.all()
    return render(request, "all_films.html", {"film": film})


def film_detail(request, id):
    show =get_object_or_404(models.Film, id=id)
    return render(request, "film_detail.html", {"film":show})


def director(request, id):
    director =get_object_or_404(models.Director, id=id)
    return render(request, 'director_id.html',{'director':director} )
