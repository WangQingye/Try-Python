import random
# 在a-b区间取整数
def getRandomInt(a,b):
    return random.randint(a,b)
# 取一个随机小于1的小数，保留a位
def getRandomfloat(a):
    return round(random.random(),a)
print(getRandomfloat(1))
