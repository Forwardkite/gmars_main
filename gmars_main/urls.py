from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from  django.conf.urls.static import static


urlpatterns = [
    path('', include('gmars_group.urls')),
    path('hiring/', include('gmars_hiring.urls')),
    path('eduhub/', include('gmars_eduhub.urls')),
    path('holidays/', include('gmars_holidays.urls')),
    path('events/', include('gmars_events.urls')),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
