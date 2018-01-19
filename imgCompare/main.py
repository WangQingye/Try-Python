from PIL import Image, ImageGrab
import pytesseract
from compareImg import compareImg
from utils import *
from pymouse import PyMouse
import time
mouse = PyMouse()
# im2 = ImageGrab.grab((619, 664, 777, 712))
# im2.save('petshangjiao.jpg', 'jpeg')

shimen = True;
baotu = True;
#师门
while shimen:
    if checkPos(806, 722, 909, 768, 'imgs/use.jpg', 857,744) == False :
        if checkPos(738, 729, 917, 780, 'imgs/goumai.jpg', 826,754) == False : 
            if checkPos(774, 716, 952, 771, 'imgs/petgoumai.jpg', 863,746) == False : 
                if checkPos(755, 662, 894, 711, 'imgs/shangjiao.jpg', 825,685) == False : 
                    if checkPos(619, 664, 777, 712, 'imgs/petshangjiao.jpg', 700,687) == False : 
                        checkPos(809, 271, 828, 290, 'imgs/shimen.jpg', 906,310)
    #等待时间在1-5s随机取
    time.sleep(getRandomInt(1,5))

#开始打图
def startBaotu():
    mouse.click(31,144) # 大地图
    time.sleep(2)
    mouse.click(480,540) # 选择长安
    time.sleep(2)
    mouse.click(133,141) # 长安地图
    time.sleep(2)
    mouse.press(706,515) # 店小二
    time.sleep(15)
    mouse.click(860,650) # 选择店小二
    time.sleep(2)        
    mouse.click(910,390) # 宝图任务


# mouse_drag(438,284,438,0)