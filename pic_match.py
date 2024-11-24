import cv2
import numpy as np

def get_xy(ref_img_path):
    """
    根据模板进行匹配，找寻图中存在的点的位置。
    :param ref_img_path:
    :return:
    """
    img_ref = cv2.imread(ref_img_path)
    img = cv2.imread('online.png')
    height, width = img_ref.shape[:2]
    # 开始模版匹配
    result = cv2.matchTemplate(img,img_ref,cv2.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,upper_left_xy = cv2.minMaxLoc(result) # 第四个元组成员才返回左上角的值。。
    lower_right_xy = (upper_left_xy[0] + width, upper_left_xy[1] + height)

    return max_val,upper_left_xy,lower_right_xy

