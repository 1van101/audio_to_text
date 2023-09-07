from django.urls import path
from audio_to_text.audios.views import AudioAddView, AudioTranscribeView

urlpatterns = (
    path('add/', AudioAddView.as_view(), name='audio_add'),
    path('audio/<int:pk>/transcribe', AudioTranscribeView.as_view(), name='audio_transcribe'),
)
