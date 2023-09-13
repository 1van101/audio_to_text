from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('audio_to_text.common.urls')),
    path('', include('allauth.urls')),
    path('accounts/', include('audio_to_text.accounts.urls')),
    path('audios/', include('audio_to_text.audios.urls')),
    path('photos/', include('audio_to_text.photos.urls')),
    path('documents/', include('audio_to_text.documents.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
