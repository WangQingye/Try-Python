from PIL import Image
# 取得某张图片的hash值
def getImageHash(path):
    img = Image.open(path)
    img = img.resize((12, 12))
    img = img.convert("L")
    imgW, imgH = img.size
    garyAvg = getGaryAvg(img)
    bitls = '' #这就是本图片的hash字符串，获取的方式主要是每个点跟平均灰度值的对比
    for h in range (1, imgH):
        for w in range (1, imgW):
             if img.getpixel((w,h)) >= garyAvg :
                 bitls = bitls + '1'
             else:
                 bitls = bitls + '0'
    return bitls

# 取得某张图片的平均灰度值
def getGaryAvg(img):
    tmpls = []
    imgW, imgH = img.size    
    for h in range (1, imgH):
        for w in range (1, imgW):
            tmpls.append(img.getpixel((w,h)))
    return sum(tmpls)/len(tmpls)

# 对比hash值的函数，得出相似度
def getPercent(a,b):
    per = 0;
    for i in range (0, len(a)):
        if a[i] == b[i]:
            per = per + 1
    return per

def compareImg(pathA, pathB):
    a = getImageHash(pathA)
    b = getImageHash(pathB)
    per =  getPercent(a,b)
    print ('图片相似度:' + str(per))
    return per