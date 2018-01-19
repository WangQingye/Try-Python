import random
from PIL import Image, ImageGrab
import pytesseract
from compareImg import compareImg
from utils import *
from pymouse import PyMouse
import win32api
import win32con
import time
mouse = PyMouse()
# 检测某一个区位
def checkPos (x1,y1,x2,y2,imgName,clickX,clickY) :
    im2 = ImageGrab.grab((x1, y1, x2, y2))
    im2.save('now.jpg', 'jpeg')
    if compareImg('now.jpg', imgName) > 100 :
        print ('执行点击' + imgName)
        # mouse.click(857,744) 
        # 如果是购买需要先点一下商品
        if imgName == 'goumai.jpg' :
            mouse.press (460, 370)
            time.sleep(getRandomfloat(1))
            mouse.release(460, 370)
        mouse.press(clickX,clickY)
        # 点击时间也要随机
        time.sleep(getRandomfloat(1))
        mouse.release(clickX,clickY)
        return True
    else :
        return False
# 在a-b区间取整数
def getRandomInt(a,b):
    return random.randint(a,b)
# 取一个随机小于1的小数，保留a位
def getRandomfloat(a):
    return round(random.random(),a)
print(getRandomfloat(1))



SW = 1920
SH = 1080
# pymouse无法实现拖拽，固重新编写一个拖拽函数
def mouse_drag(x,y,x2,y2):
    mouse.move(x,y)
    # windll.user32.SetCursorPos(x, y)    #鼠标移动到  
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)    #左键按下
    time.sleep(0.2)
    mw = int(x2 * 65535 / SW) 
    mh = int(y2 * 65535 / SH)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)    
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)