from tkinter import *
import keyboard
import cv2.cv2 as cv2
from PIL import ImageGrab
import numpy as np
import mouse
import time


def screenshot(x1, y1, x2, y2):
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    im = np.array(im)
    cv_img = im.astype(np.uint8)
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    cv_img = 255-cv_img
    cv2.imwrite('img.png', cv_img)



def drag_range():
    root = Tk()
    toplevel = Toplevel(root)
    canvas = Canvas(toplevel, highlightthickness=0, bd=0, relief='ridge', bg='white')
    canvas.master.wm_attributes('-transparentcolor', 'white')
    canvas.pack(expand=True, fill="both")

    # 화면 반짝거림 줄이기
    toplevel.update()

    # 전체화면, 맨위, 창 상단바 없애기
    toplevel.attributes('-fullscreen', True)
    toplevel.wm_attributes('-topmost', True)
    toplevel.focus_force()
    toplevel.overrideredirect(True)
    toplevel.update()

    # Crop할 부분 사각형 처리 및 좌표 가져오기 (마우스 왼쪽 버튼 클릭)

    is_first_click = False
    start_point = True
    spos_x, spos_y = 0, 0
    while True:
        if keyboard.is_pressed('f8'):
            if start_point:
                spos_x, spos_y = mouse.get_position()
                canvas.create_rectangle(0, 0, 0, 0, tags="rect")
                start_point = False
            curpos_x, curpos_y = mouse.get_position()
            canvas.delete("rect")
            canvas.create_rectangle(spos_x, spos_y, curpos_x, curpos_y, outline='red', tags="rect", width=2)
            canvas.update()
            time.sleep(0.01)
            is_first_click = True
        if not keyboard.is_pressed('f8') and is_first_click:
            epos_x, epos_y = mouse.get_position()
            x2, y2 = epos_x, epos_y
            #           시작x    시작y    끝x      끝y
            toplevel.destroy()
            toplevel.update()
            break
    toplevel.destroy()
    toplevel.update()
    return spos_x, spos_y, epos_x, epos_y