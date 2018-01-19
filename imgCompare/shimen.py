import sys
sys.path.append('./tools')
from vender import *
#师门
def startShimen():
    while shimen:
        if checkPos(806, 722, 909, 768, 'imgs/use.jpg', 857,744) == False :
            if checkPos(738, 729, 917, 780, 'imgs/goumai.jpg', 826,754) == False : 
                if checkPos(774, 716, 952, 771, 'imgs/petgoumai.jpg', 863,746) == False : 
                    if checkPos(755, 662, 894, 711, 'imgs/shangjiao.jpg', 825,685) == False : 
                        if checkPos(619, 664, 777, 712, 'imgs/petshangjiao.jpg', 700,687) == False : 
                            checkPos(809, 271, 828, 290, 'imgs/shimen.jpg', 906,310)
        #等待时间在1-5s随机取
        time.sleep(getRandomInt(1,5))
    return True