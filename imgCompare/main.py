from PIL import Image, ImageGrab
import pytesseract
from compareImg import compareImg
from utils import *
from pymouse import PyMouse
import time
mouse = PyMouse()
# im2 = ImageGrab.grab((619, 664, 777, 712))
# im2.save('petshangjiao.jpg', 'jpeg')
while True:
    if checkPos(806, 722, 909, 768, 'use.jpg', 857,744) == False :
        if checkPos(738, 729, 917, 780, 'goumai.jpg', 826,754) == False : 
            if checkPos(774, 716, 952, 771, 'petgoumai.jpg', 863,746) == False : 
                if checkPos(755, 662, 894, 711, 'shangjiao.jpg', 825,685) == False : 
                    if checkPos(619, 664, 777, 712, 'petshangjiao.jpg', 700,687) == False : 
                        checkPos(809, 271, 828, 290, 'shimen.jpg', 906,310)
    #等待时间在1-5s随机取
    time.sleep(getRandomInt(1,5))