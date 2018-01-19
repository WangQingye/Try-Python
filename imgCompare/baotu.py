import sys
sys.path.append('./tools')
from vender import *
# 开始打图
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

def startWatu():
    mouse.click(984,743)
    time.sleep(1)            
    for line in range(0,4) :
        im2 = ImageGrab.grab((516, 311+line*81, 582, 311+line*81+66))
        im2.save('imgs/wupin.jpg', 'jpeg')
        if compareImg('imgs/wupin.jpg', 'imgs/baotu.jpg') > 100 :
            print('找到了宝图，在第'+ str(line+1) + '行')
            mouse.click(552,311+line*81 + 40) # 双击宝图会直接执行挖图
            # mouse.click(392,569)
            break
        print ('开始找下一行')
startWatu()