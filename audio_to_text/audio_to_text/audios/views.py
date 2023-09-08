from celery.result import AsyncResult
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from django.views import generic as views

from audio_to_text.audios.forms import AudioAddForm
from audio_to_text.audios.models import Audio
from audio_to_text.audios.tasks import transcribe_audio
from utils import helpers
from utils.helpers import download_word_document

UserModel = get_user_model()


class AudioAddView(LoginRequiredMixin, views.CreateView):
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

        audio_text_task = transcribe_audio.delay(path)
        audio.extracted_text_task_id = audio_text_task.id

        audio.save()

        return super().form_valid(form)


class AudioTranscribeView(LoginRequiredMixin, views.DetailView):
    template_name = 'audios/audio-transcribe-page.html'
    model = Audio

    def get_object(self, queryset=None):
        audio = super().get_object(queryset=queryset)

        audio_text_task_id = audio.extracted_text_task_id

        if audio_text_task_id:
            result = AsyncResult(audio_text_task_id)
            if result.ready():
                audio.extracted_text = result.result
                audio.extracted_text_task_id = None
                audio = helpers.create_and_save_word_document(audio, audio.extracted_text)
                audio.save()

        return audio


class AudioTextDownloadView(LoginRequiredMixin, views.View):
    def get(self, request, pk):
        audio_text = get_object_or_404(Audio, pk=pk)
        word_file_path = audio_text.word_document

        return download_word_document(audio_text, word_file_path)
