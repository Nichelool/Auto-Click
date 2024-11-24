from do_click import doClick
from pic_match import get_xy
from hwnd_screenshot import get_hwnd,screenshot
import random
import time

def click_random(ref_img_path,handle,child):
    screenshot(handle, 1.5)
    max_val = 0.5
    while max_val < 0.95:
        screenshot(handle, 1.5)
        max_val,l_xy, r_xy = get_xy(ref_img_path)
        time.sleep(0.1)
        # print(max_val)
    lx = int((l_xy[0] - 5) / 1.5)
    ly = int((l_xy[1] - 54) / 1.5)
    rx = int((r_xy[0] - 5)/ 1.5)
    ry = int((r_xy[1] - 54) / 1.5)
    x_target = random.randint(lx, rx)
    y_target = random.randint(ly, ry)
    doClick(x_target,y_target,child)

    return

if __name__ == '__main__':
    window_title = 'MuMu模拟器0'
    hwnd, cld = get_hwnd(window_title)
    click_random('./pics/k28/k28_s.png',hwnd,cld)