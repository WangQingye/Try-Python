import random
from PIL import Image, ImageGrab
import pytesseract
from compareImg import compareImg
from utils import *
from pymouse import PyMouse
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
