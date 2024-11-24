import win32api
import win32con
import time

def doClick(cx,cy,hwnd):
    """
    实现后台点击
    :param cx:相对于句柄初始左上坐标的偏移x
    :param cy: 相对于句柄初始左上坐标的偏移y
    :param hwnd: 一般要涉及到子窗口句柄
    :return: 返回空，仅实现点击功能
    """
    long_position = win32api.MAKELONG(cx,cy)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    time.sleep(0.1)
    win32api.SendMessage(hwnd,win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,long_position)
    return


