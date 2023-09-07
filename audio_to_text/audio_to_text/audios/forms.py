from django import forms

from audio_to_text.audios.models import Audio


class AudioAddForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'audio_file']

