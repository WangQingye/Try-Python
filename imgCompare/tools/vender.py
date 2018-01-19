# 要引用的库统一写在这里，免得每个都要引用
from PIL import Image, ImageGrab
import pytesseract
from compareImg import compareImg
from utils import *
from pymouse import PyMouse
import time
mouse = PyMouse()