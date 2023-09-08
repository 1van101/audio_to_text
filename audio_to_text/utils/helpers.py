import datetime
import os

import docx
from django.http import FileResponse, HttpResponse
from django.urls import reverse_lazy, reverse
from googletrans import Translator

from audio_to_text import settings


def translate_text(content, lang):
    translator = Translator()
    try:
        translated_content = translator.translate(content, dest=lang)
        translated_text = translated_content.text
    except Exception as e:
        translated_text = f"Translation Error: {str(e)}"

    return translated_text


def save_word_document(doc):
    media_root = settings.MEDIA_ROOT
    temp_file_path = os.path.join(media_root, 'word_documents', 'temp.docx')

    doc.save(temp_file_path)

    return temp_file_path


def create_and_save_word_document(document, extracted_text):
    doc = docx.Document()
    doc.add_paragraph(extracted_text)
    word_file_path = save_word_document(doc)
    document.word_document = word_file_path
    return document


def download_word_document(document, word_file_path):
    with open(word_file_path, 'rb') as word_file:
        content = word_file.read()

        response = HttpResponse(
            content,
            # content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")
        response['Content-Disposition'] = f'attachment; filename="{formatted_datetime}-{document.title}.docx"'
        response['Content-Length'] = len(content)  # calculate length of content

        return response
