import mouse

from drag_shot import drag_range, screenshot
from pretreatment import process_image_for_ocr
from from_img_to_text import im_to_text
from transfer1 import trans_text
from time import sleep
import cv2.cv2 as cv2



flag = False
x, y, x1, y1 = drag_range()

def a(hold):
    screenshot(x, y, x1, y1)
    im = process_image_for_ocr('img.png', hold)
    cv2.imwrite('cvt_img.png', im)
    text = im_to_text()
    final_trans = trans_text(text)
    return text, final_trans

if __name__ == '__main__':
    save_text = ''
    while 1:
        ja, ko = a(42)
        if save_text != ja:
            print(ja)
            print(ko)
            save_text = ja





