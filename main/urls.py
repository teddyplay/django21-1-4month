from django.urls import path
from . import views


urlpatterns = [

    path('about_us/', views.abous_us),
    path('date_now/', views.date_now),
    path('all_films/', views.film_show),
    path('all_films/<int:id>', views.film_detail),


]
