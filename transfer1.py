import googletrans
from googletrans import Translator
from time import time

# print(googletrans.LANGUAGES)
translator = Translator()

def trans_text(text1):
    try:
        text = text1
        trans1 = translator.translate(text, src='ja', dest='ko')
        # print("번역 완료: ", trans1.text)
        text = trans1.text
    except:
        text = ""
    return text

