from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('gmars_group.urls')),
    path('hiring/', include('gmars_hiring.urls')),
    path('eduhub/', include('gmars_eduhub.urls')),
    path('holidays/', include('gmars_holidays.urls')),
    path('events/', include('gmars_events.urls')),
    path('admin/', admin.site.urls)
]




