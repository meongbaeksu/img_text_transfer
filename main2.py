import mouse

from drag_shot import drag_range, screenshot
from pretreatment import process_image_for_ocr
from from_img_to_text import im_to_text
from transfer1 import trans_text
from time import sleep
import cv2.cv2 as cv2



flag = False
x, y, x1, y1 = drag_range()

save_text = ''
def a(hold, im_size):
    global save_text
    screenshot(x, y, x1, y1)
    im = process_image_for_ocr(hold, im_size)
    cv2.imwrite('cvt_img.png', im)
    text = im_to_text()
    if save_text != text:
        final_trans = trans_text(text)
        save_text = text
        print(text)
        print(final_trans)
# hold= 20 im_size= 1150
if __name__ == '__main__':
    for i in range(10, 100, 10):
        for j in range(100, 5000, 300):
            print('hold=', i, 'im_size=', j)
            a(hold=i, im_size=j)



