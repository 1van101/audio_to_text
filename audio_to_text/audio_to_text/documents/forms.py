from django import forms

from audio_to_text.documents.models import Document
import utils


class DocumentTranslateLanguageForm(forms.Form):
    language_choices = [(code, name) for code, name in utils.supported_languages.supported_languages.items()]
    selected_language = forms.ChoiceField(choices=language_choices)


class DocumentAddForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'document_file']
