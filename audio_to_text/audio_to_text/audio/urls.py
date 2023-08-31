from django.urls import path, include

from audio_to_text.audio.views import AudioAddView, AudioDetailsView, AudioTranscribeView

urlpatterns = (
    path('add/', AudioAddView.as_view(), name='audio_add'),
    path('audio/<int:pk>/', include([
        path('', AudioDetailsView.as_view(), name='audio_details'),
        path('transcribe/', AudioTranscribeView.as_view(), name='audio_transcribe'),
    ]
    ))

)
