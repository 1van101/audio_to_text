from django.urls import path

from audio_to_text.photos.views import PhotoAddView, PhotoTranslateView

urlpatterns = (
    path('add/', PhotoAddView.as_view(), name='photo_add'),
    path('photo/<int:pk>/translate/', PhotoTranslateView.as_view(), name='photo_translate'),

)
