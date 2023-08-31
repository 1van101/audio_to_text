from django import forms
from . import supported_languages
from audio_to_text.photos.models import Photo


class PhotoTranslateLanguageForm(forms.Form):
    language_choices = [(code, name) for code, name in supported_languages.supported_languages.items()]
    selected_language = forms.ChoiceField(choices=language_choices)


class PhotoAddForm(forms.ModelForm):
    class Meta:

        model = Photo
        fields = ['title', 'photo_file', 'language']


