from PIL import Image
import pytesseract

def im_to_text(path = 'cvt_img.png'):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(path), lang='jpn')
    # print(text.replace(" ", "").replace("\n", ''))
    text = text.replace(" ", "").replace("\n", '')
    return text
