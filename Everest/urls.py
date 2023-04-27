from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from Everest import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('course/', include('Course.urls')),
    path('location/', include('location.urls')),
    path('teacher/', include('Teacher.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
