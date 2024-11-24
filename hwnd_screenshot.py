import win32gui
import cv2
import numpy as np
import win32ui
import win32con

def get_hwnd(name):
    """
    用于获取指定名称的窗口句柄
    :param name: 窗口名
    :return: 窗口句柄
    """
    hwnd = win32gui.FindWindow(None, name)
    children = win32gui.FindWindowEx(hwnd, None, None, None)

    return hwnd, children

def screenshot(hwnd,zoom):
    """
    还需要改进一下。
    :param hwnd:等待被截图的窗口句柄
    :param zoom: 当前计算机设备采用的缩放比
    :return: 左上角的点坐标(x,y)和图像数据img
    """
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitmap = win32ui.CreateBitmap()
    x, y, x2, y2 = win32gui.GetWindowRect(hwnd)
    a = x2 - x
    b = y2 - y
    width = int((x2 - x) * zoom)
    height = int((y2 - y) * zoom)
    saveBitmap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitmap)
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
    signedIntsArray = saveBitmap.GetBitmapBits(True)
    in_opencv = np.frombuffer(signedIntsArray, dtype=np.uint8)
    in_opencv.shape = (height, width, 4)
    img = cv2.cvtColor(in_opencv, cv2.COLOR_BGRA2BGR)
    # img2 = cv2.resize(img,(a,b), interpolation=cv2.INTER_LANCZOS4) # 这一步不需要了，因为保存到本地的分辨率就是实际大小。
    # 释放内存
    win32gui.DeleteObject(saveBitmap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    cv2.imwrite('now.png', img)

    return


if __name__ == '__main__':
    zoom_eff = 1.5
    window_title = 'MuMu模拟器1'
    handle, child = get_hwnd(window_title)
    x,y,img = screenshot(handle, zoom_eff)
    # print(x,y)
    # cv2.imshow('img', img)
    cv2.imwrite('online.png', img)
    # cv2.waitKey(0)