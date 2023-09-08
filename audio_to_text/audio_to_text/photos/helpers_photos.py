from PIL import Image
from pytesseract import pytesseract
import platform


def extract_text_from_image(lang, uploaded_photo):


    current_os = platform.system()

    if current_os == 'Windows':
        pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    elif current_os == 'Linux':
        pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    elif current_os == 'Darwin':  # macOS
        pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
    else:
        print("Unsupported operating system")

    img = Image.open(uploaded_photo)
    text = pytesseract.image_to_string(img, lang=lang)
    return text
