from django.urls import path

from audio_to_text.photos.views import PhotoAddView, PhotoTranslateView, PhotoTextDownloadView

urlpatterns = (
    path('add/', PhotoAddView.as_view(), name='photo_add'),
    path('photo/<int:pk>/translate/', PhotoTranslateView.as_view(), name='photo_translate'),
    path('photo/<int:pk>/download/', PhotoTextDownloadView.as_view(), name='photo_download'),
)
