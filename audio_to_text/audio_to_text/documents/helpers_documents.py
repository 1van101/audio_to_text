import os
import tempfile

import PyPDF2


def extract_text_from_pdf(pdf_file):
    text = ""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir, 'temp.pdf')
        with open(temp_file_path, 'wb+') as temp_file:
            for chunk in pdf_file.chunks():
                temp_file.write(chunk)

        pdf_document = PyPDF2.PdfReader(temp_file_path)
        num_pages = len(pdf_document.pages)
        for page_num in range(num_pages):
            page = pdf_document.pages[page_num]
            text += page.extract_text()

    return text


