from PIL import Image
from googletrans import Translator
from pytesseract import pytesseract


def extract_text(lang, uploaded_photo):
    img = Image.open(uploaded_photo)

    # TODO with rest!
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    return pytesseract.image_to_string(img, lang=lang)


def translate_text(content, lang):
    translator = Translator()
    try:
        translated_content = translator.translate(content, dest=lang)
        translated_text = translated_content.text
    except Exception as e:
        translated_text = f"Translation Error: {str(e)}"

    return translated_text
