from django.contrib.auth.mixins import LoginRequiredMixin

from . import helpers
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from . import supported_languages
from audio_to_text.photos.forms import PhotoAddForm, PhotoTranslateLanguageForm
from audio_to_text.photos.models import Photo

UserModel = get_user_model()


class PhotoAddView(LoginRequiredMixin, views.CreateView):
    template_name = 'photos/photo-add-page.html'
    model = Photo
    form_class = PhotoAddForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        photo = form.save(commit=False)

        user_instance = UserModel.objects.get(pk=self.request.user.pk)

        photo.user = user_instance

        uploaded_photo = form.cleaned_data['photo_file']
        selected_lang = form.cleaned_data.get('language')
        extracted_text = helpers.extract_text(selected_lang, uploaded_photo)
        photo.extracted_text = extracted_text

        photo.save()

        return super().form_valid(form)


class PhotoTranslateView(LoginRequiredMixin, views.FormView):
    template_name = 'photos/photo-translate-page.html'
    model = Photo
    form_class = PhotoTranslateLanguageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = get_object_or_404(Photo, pk=self.kwargs['pk'])
        context['lang'] = supported_languages.supported_languages
        context['original_content'] = photo.extracted_text
        context['photo'] = photo
        return context

    def form_valid(self, form):
        photo = get_object_or_404(Photo, pk=self.kwargs['pk'])
        original_content = photo.extracted_text
        selected_lang = form.cleaned_data['selected_language']

        translated_text = helpers.translate_text(original_content, selected_lang)

        context = {
            'original_content': original_content,
            'translated_content': translated_text,
            'lang': supported_languages.supported_languages,
            'form': form,
            'photo': photo
        }

        return self.render_to_response(context)
