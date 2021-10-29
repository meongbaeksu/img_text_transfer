import tempfile

import cv2.cv2 as cv2
import numpy as np
from PIL import Image
import time

def process_image_for_ocr(THREHOLD, img_size, file_path='img.png'):
    # TODO : Implement using opencv
    temp_filename = set_image_dpi(file_path, img_size)
    im_new = remove_noise_and_smooth(temp_filename, THREHOLD)
    return im_new

def set_image_dpi(file_path, img_size):
    a = time.time()
    im = Image.open(file_path)
    # print(im.size)
    length_x, width_y = im.size
    factor = max(1, int(img_size / length_x))
    size = factor * length_x, factor * width_y
    # size = (1800, 1800)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300, 300))
    # print(time.time()-a)
    return temp_filename

def image_smoothening(img, THREHOLD):
    ret1, th1 = cv2.threshold(img, THREHOLD, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(th2, (1, 1), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th3

def remove_noise_and_smooth(file_name, THREHOLD):
    img = cv2.imread(file_name, 0)
    filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41,
                                     3)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    img = image_smoothening(img, THREHOLD)
    or_image = cv2.bitwise_or(img, closing)
    return or_image