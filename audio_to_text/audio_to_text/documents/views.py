from django.contrib.auth.mixins import LoginRequiredMixin

from utils import helpers, supported_languages
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from audio_to_text.documents import helpers_documents
from audio_to_text.documents.forms import DocumentAddForm, DocumentTranslateLanguageForm
from audio_to_text.documents.models import Document
from utils.helpers import download_word_document

UserModel = get_user_model()


class DocumentAddView(LoginRequiredMixin, views.CreateView):
    template_name = 'documents/document-add-page.html'
    model = Document
    form_class = DocumentAddForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        document = form.save(commit=False)

        user_instance = UserModel.objects.get(pk=self.request.user.pk)
        document.user = user_instance
        uploaded_document = form.cleaned_data['document_file']
        extracted_text = helpers_documents.extract_text_from_pdf(uploaded_document)
        document.extracted_text = extracted_text

        document = helpers.create_and_save_word_document(document, extracted_text)

        document.save()

        return super().form_valid(form)


class DocumentTranslateView(LoginRequiredMixin, views.FormView):
    template_name = 'documents/document-translate-page.html'
    model = Document
    form_class = DocumentTranslateLanguageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        document = get_object_or_404(Document, pk=self.kwargs['pk'])

        context.update({
            'original_content': document.extracted_text,
            'document': document
        })
        return context

    def form_valid(self, form):
        document = get_object_or_404(Document, pk=self.kwargs['pk'])
        original_content = document.extracted_text
        selected_lang = form.cleaned_data['selected_language']

        translated_text = helpers.translate_text(original_content, selected_lang)

        context = {
            'original_content': original_content,
            'translated_content': translated_text,
            'lang': supported_languages.supported_languages,
            'form': form,
            'document': document
        }

        return self.render_to_response(context)


class DocumentDownloadView(LoginRequiredMixin, views.View):
    def get(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        word_file_path = document.word_document
        return download_word_document(document, word_file_path)
