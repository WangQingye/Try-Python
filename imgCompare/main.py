import sys
sys.path.append('./tools')
from vender import *

# im2 = ImageGrab.grab((516, 473, 582, 539))
# im2.save('imgs/baotu.jpg', 'jpeg')

shimen = True;
baotu = True;

# 在活动栏中截取任务图标
def grabIcons():
    for line in range (0,3) :
        im2 = ImageGrab.grab((232, 301 + line * 103, 298, 334 + line * 103))
        im2.save('imgs/l'+str(line)+'.jpg', 'jpeg')
        time.sleep(0.5)
        im2 = ImageGrab.grab((598, 301 + line * 103, 664, 334 + line * 103))
        im2.save('imgs/r'+str(line)+'.jpg', 'jpeg')
# mouse_drag(414,299,414,0)

grabIcons()