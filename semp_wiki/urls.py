from django.contrib import admin
from django.urls import path, include, re_path
from status_page.views import landing
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('status_page.urls')),
    path('servers/', include('servers.urls')),
    path('wiki/', include('core_wiki.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
