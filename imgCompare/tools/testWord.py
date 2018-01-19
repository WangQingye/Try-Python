from PIL import Image, ImageGrab
import pytesseract
text=pytesseract.image_to_string(Image.open('111.png'),lang='chi_sim') #设置为中
print(text)
im = Image.open('1.jpg')
im = im.convert("L")
im.save('11.jpg', 'jpeg')