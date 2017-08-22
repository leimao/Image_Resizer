# Image Resizer
# Author: Lei Mao
# Institution: University of Chicago
# Date: 8/22/2017
# Python: 3.6


import cv2

def resizer_ratio(img_path, img_name, fx = 1, fy = 1):
    img_name_prefix = img_name.split('.')[0]
    img = cv2.imread(img_path + img_name)
    res = cv2.resize(src = img, dsize = None, fx = 0.2, fy = 0.2, interpolation = cv2.INTER_AREA)
    cv2.imwrite(filename = img_path + img_name_prefix + '_resized.png', img = res)
    return

def resizer_defined(img_path, height = None, width = None):
    img_name_prefix = img_name.split('.')[0]
    img = cv2.imread(img_path + img_name)
    res = cv2.resize(src = img, dsize = (width, height), fx = 0, fy = 0, interpolation = cv2.INTER_AREA)
    cv2.imwrite(filename = img_path + img_name_prefix + '_resized.png', img = res)
    return 





