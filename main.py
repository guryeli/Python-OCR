import fitz
from PIL import Image
import pytesseract


def getSupportedLanguageCodes():
    lang_codes = pytesseract.get_languages()
    print("Supported Lang Codes:")
    for lang_code in lang_codes:
        print(lang_code)


def imageOCR(image_path, lang='tur'):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang=lang)
    return text

def pdfOCR(pdf_path, lang='tur'):
    pdf_file = fitz.open(pdf_path)
    total_page = pdf_file.page_count

    for page_no in range(total_page):
        page = pdf_file[page_no]

        if page.get_text("text"):
            text = page.get_text("text")
            print(f"Page {page_no + 1} Text:\n{text}")

        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text = pytesseract.image_to_string(img, lang=lang)
        print(f"Page {page_no + 1} Image Text:\n{text}")

    pdf_file.close()

print(getSupportedLanguageCodes())