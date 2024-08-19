from django.urls import path
from . import views


urlpatterns = [
    path('', views.events_home, name="events-home"),
    path('about/', views.events_about, name="events-about"),
    path('cars/', views.events_cars, name="events-cars"),
    path('corporate/', views.events_corporate, name="events-corporate"),
    path('contact/', views.events_contact, name="events-contact"),
]
