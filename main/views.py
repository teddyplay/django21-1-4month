from django.shortcuts import render
import datetime

def abous_us(request):
    return render(request, 'about_us.html')


def date_now(request):
    a = datetime.datetime.now()
    return render(request, 'date_now.html', {'a':a})
