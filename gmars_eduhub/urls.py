from django.urls import path
from . import views


urlpatterns = [
    path('', views.eduhub_home, name='eduhub-home'),
    path('about/', views.eduhub_about, name='eduhub-about'),
    path('service/', views.eduhub_service, name='eduhub-service'),
    path('contact/', views.eduhub_contact, name='eduhub-contact'),
]


