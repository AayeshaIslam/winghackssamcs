import pytesseract
from pdf2image import convert_from_path


pdf_path = "testrudeimage.pdf"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_text_ocr(pdf_path):
    """
    Extracts text from an image-based (scanned) PDF using OCR.
    """
    text = ""
    images = convert_from_path(pdf_path)
    for image in images:
        text += pytesseract.image_to_string(image, lang="eng") + "\n"

    return text.strip()


extracted_text = extract_text_ocr(pdf_path)


print(extracted_text)


with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(extracted_text)

print("\nExtracted text has been saved to 'extracted_text.txt'")
