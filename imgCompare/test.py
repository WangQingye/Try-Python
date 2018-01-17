from PIL import Image, ImageFilter, ImageGrab
from compareImg import compareImg
from pymouse import PyMouse
import time
mouse = PyMouse()
# mouse.click(100,100)
im2 = ImageGrab.grab((811, 660, 915, 710))
im2.save('now.jpg', 'jpeg')
if compareImg('now.jpg', 'use.jpg') > 1 :
    # mouse.click(650,1060)
    # mouse.click(863,685)
    print (1)
    mouse.click(100,100)    
    time.sleep(1)    
    mouse.press(863,685)
    print (2)    
    time.sleep(2)
    mouse.release(863,685)

# compareImg('test/TEST1/1.jpg', 'test/TEST1/2.jpg')
# mouse.press(709,118)
# time.sleep(2)
# mouse.release(709,118)
