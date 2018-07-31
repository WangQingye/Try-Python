# 二分查找就是在有序元素中以中位数开始查找
# 简单例子是 1-100 的猜数游戏中以50开始查询
# 又或者是要查一个首字母为M的单词，可以从字典的中间开始往后翻

# 代码实例：
import math
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        # 从中间部分开始查找
        mid = math.ceil((low + high) / 2)
        guess = list[mid]
        # print (guess)
        # 如果等于，说明找到了
        if guess == item:
            return mid
        # 如果大于，说明数字大了，那么修改high值为mid-1
        if guess > item:
            high = mid - 1
        # 如果小于，说明数字小了，修改low值为mid+1
        else:
            low = mid + 1
    # 如果没找到
    return None

# 代码测试
my_list = [1,3,5,7,9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))