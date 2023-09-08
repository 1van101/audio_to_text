from django.urls import path

from audio_to_text.documents.views import DocumentAddView, DocumentTranslateView,DocumentDownloadView

urlpatterns = (
    path('add/', DocumentAddView.as_view(), name='document_add'),
    path('document/<int:pk>/translate/', DocumentTranslateView.as_view(), name='document_translate'),
    path('document/<int:pk>/download/', DocumentDownloadView.as_view(), name='document_download'),

)
