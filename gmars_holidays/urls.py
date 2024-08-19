from django.urls import path
from . import views


urlpatterns = [
    path('', views.holidays_home, name='holidays-home'),
    path('holidays_about/', views.holidays_about, name='holidays-about'),
    path('holidays_booking/', views.holidays_booking, name='holidays-booking'),
    path('holidays_umrah/', views.holidays_umrah, name='holidays-umrah'),
    path('holidays_tour/', views.holidays_tour, name='holidays-tour'),
    path('views.holidays_visa/', views.holidays_visa, name='holidays-visa'),
    path('views.holidays_contact/', views.holidays_contact, name='holidays-contact'),
]