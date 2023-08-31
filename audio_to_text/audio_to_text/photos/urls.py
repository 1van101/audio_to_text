from django.urls import path, include

from audio_to_text.photos.views import PhotoAddView, PhotoDetailsView, PhotoTranslateView

urlpatterns = (
    path('add/', PhotoAddView.as_view(), name='photo_add'),
    path('photo/<int:pk>/', include([
        path('', PhotoDetailsView.as_view(), name='photo_details'),
        path('translate/', PhotoTranslateView.as_view(), name='photo_translate'),
        ]
    ))

)
