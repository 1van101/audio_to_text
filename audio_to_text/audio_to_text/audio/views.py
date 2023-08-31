from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from audio_to_text.audio.forms import AudioAddForm
from audio_to_text.audio.models import Audio

import whisper
from pydub import AudioSegment

UserModel = get_user_model()


class AudioAddView(views.CreateView):
    template_name = 'audios/audio-add-page.html'
    model = Audio
    form_class = AudioAddForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        audio = form.save(commit=False)
        user = UserModel.objects.get(pk=self.request.user.pk)
        audio.user = user

        audio.save()
        path = audio.audio_file.path

        audio_text = self.transcribe_audio(path)

        audio.extracted_text = audio_text
        audio.save()

        return super().form_valid(form)

    @staticmethod
    def transcribe_audio(audio_file_path):
        model = whisper.load_model("base")
        transcription = model.transcribe(audio_file_path, fp16=False)
        return transcription['text']


class AudioDetailsView(views.DetailView):
    pass


class AudioTranscribeView(views.FormView):
    pass
