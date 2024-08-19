from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.hiring_home, name="hiring-home"),
    path('about/', views.hiring_about, name="hiring-about"),
    path('service/', views.hiring_service, name="hiring-service"),
    path('contact/', views.hiring_contact, name="hiring-contact"),
    path('jobs/', views.hiring_jobs, name="hiring-jobs"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



